# 2025年10月30日 每日总结


## 💡 心得感悟
      知识点：
          一、C语言：      
                      1、while循环语句中的contiue出现直接略过后面，返回判断的地方。
                      2、getchar和putchar。前者定义返回值为整型，定义为int 
                      3、移除函数strcspn
                       char password[20] = {0};
                       fgets(password, sizeof(password), stdin);
                       password[strcspn(password, "\n")] = '\0';
                      4、更安全的字符输入函数fgets,可以读取整行和空格
                       char input[100];
                       fgets(input, sizeof(input), stdin);
                      

          二、python：

          三、高数：
          



      
      技巧点：
            一、C语言：
                  1、注意swich+case语句中，不出现break就会逐条运行下去
                  2、注意如果getchar的输入不为整型，则会返回EOF码，表示错误，可以用作判断语句。补充也可以表示文
                  件结束
                              补充getchar是读取一个字符
                  3、注意scanf 和 getchar输入有区别，后者会读取换行\n，前者读取有空格只会读空格前面的东西
                  
                  输入输出之间还有缓冲区这个区域其中的换行\n，会等待读取，如果scanf 没读取\n 那么会留给getchar 
                  导致输入和预想产生偏差。此时我们就需要把缓冲区的\n拿走，利用getchar的性质开始逐字读取缓冲区：
                  int ch = 0;
                  while ((ch = getchar()) != '\n' && ch != EOF)
	                  ;                                    -----→空语句，表示循环体什么都不做
                  直到循环读取到换行符或文件结束
                  4、字符串的索引从0开始
                  5、fgets最多读取规定字符数-1个字符，留了一个给\0。
                        注意，使用了fgets的话，需要处理\n，建议使用strcspn.

          二、python：

          三、高数：
            

      



**自动创建时间：** Thu Oct 30 00:26:56 CST 2025
