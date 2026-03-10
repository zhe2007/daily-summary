# 2026年03月10日 每日总结


## 💡 心得感悟
      知识点：
          一、C语言：

          二、python：

          三、高数：

          四、汇编：

          五、linux指令：

          六、ctf:
          1、readelf -S pwn查看表项地址
          2、RELRO（RELocation Read-Only）是一种可选的二进制保护机制，用于增加程序的安全性。它主要
通过限制和保护全局偏移表（Global Offset Table，简称 GOT）和过程链接表（Procedure Linkage 
Table，简称 PLT）的可写性来防止针对这些结构的攻击。
          3、shellcraft 模块是 
pwntools 库中的一个子模块，用于生成各种不同体系结构的 Shellcode。
Shellcode 是一段以二进制形式编写的代码，用于利用软件漏洞、执行特定操作或获取系统权限。
shellcraft 模块提供了一系列函数和方法，用于生成特定体系结构下的 Shellcode
shellcode = asm(shellcraft.sh())                 
io.sendline(shellcode)                 
生成一个 Shellcode
# 将生成的 Shellcode 发送到目标
4、32位开启NX保护，部分开启RELRO保护
具体攻击手法为：ret2libc




      
      技巧点：
            一、C语言：

          二、python：

          三、高数：

          四、汇编：

          五、linux指令：

          六、ctf:

      



**自动创建时间：** Tue Mar 10 00:56:35 CST 2026
