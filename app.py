# Flask + SQLite + APScheduler 最小可用实现
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.getenv("DB_PATH", os.path.join(BASE_DIR, "data", "data.sqlite"))
TEMPLATE_DEFAULT = os.getenv("TEMPLATE_DEFAULT", "# 每日总结 - {{date}}\n\n- 今日完成：\n  - \n\n- 明日计划：\n  - \n\n- 收获/问题：\n  - \n")
MIN_CHARS = int(os.getenv("MIN_CHARS", "20"))

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-change-me")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///'" + DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Entry(db.Model):
    date = db.Column(db.String(20), primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

def ensure_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    if not os.path.exists(DB_PATH):
        db.create_all()

def render_template_text(d):
    return TEMPLATE_DEFAULT.replace("{{date}}", d)

def create_for_date(dstr):
    e = Entry.query.get(dstr)
    if e: return False
    content = render_template_text(dstr)
    e = Entry(date=dstr, content=content)
    db.session.add(e); db.session.commit()
    return True

def cleanup_job(min_chars=MIN_CHARS):
    entries = Entry.query.all()
    removed = 0
    for e in entries:
        cleaned = "".join(e.content.split())
        if len(cleaned) < min_chars:
            db.session.delete(e); removed += 1
    if removed>0:
        db.session.commit()
    print("cleanup done, removed:", removed)

@app.route("/")
def index():
    entries = Entry.query.order_by(Entry.date.desc()).all()
    return render_template("index.html", entries=entries)

@app.route("/create_today")
def create_today():
    d = date.today().strftime("%Y-%m-%d")
    create_for_date(d)
    return redirect(url_for("index"))

@app.route("/edit/<d>", methods=["GET","POST"])
def edit(d):
    e = Entry.query.get(d)
    if not e:
        content = render_template_text(d)
        e = Entry(date=d, content=content)
        db.session.add(e); db.session.commit()
    if request.method=="POST":
        e.content = request.form['content']
        db.session.commit()
        flash("保存成功")
        return redirect(url_for("index"))
    return render_template("edit.html", entry=e)

@app.route("/export/<d>")
def export(d):
    e = Entry.query.get(d)
    if not e:
        return "未找到", 404
    return e.content, 200, {'Content-Type': 'text/markdown; charset=utf-8'}

@app.route("/cleanup")
def cleanup_route():
    cleanup_job()
    flash("已清理空记录")
    return redirect(url_for("index"))

if __name__=="__main__":
    ensure_db()
    sched = BackgroundScheduler(daemon=True)
    # Scheduler uses server local timezone by default; change to timezone="UTC" if needed
    sched.add_job(lambda: create_for_date(date.today().strftime("%Y-%m-%d")), 'cron', hour=0, minute=5)
    sched.add_job(lambda: cleanup_job(), 'cron', hour=23, minute=55)
    sched.start()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
