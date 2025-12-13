# 2025年12月13日 每日总结


## 💡 心得感悟
      知识点：
          一、C语言：
          1、数组的[]本身就是解引用
          2、数组一般存入内存的栈中，而指针指向内存任意地方
          3、函数名就是函数的地址，就像数组名是数组的地址一样
          

          二、python：

          三、高数：

          四、汇编：

          五、linux指令：
          



      
      技巧点：
            一、C语言：
            1、数组名就是指向数组第一个元素的指针
             int N;
             scanf("%d", &N);  // 读取同学数量

             int* A = (int*)malloc(N * sizeof(int));  // 动态分配数组内存
             if (A == NULL) {  // 检查内存分配是否成功
           printf("Memory allocation failed!\n");
           return 1;
                   }
             // 读取初始座位上的学号
       for (int i = 0; i < N; i++) {
           scanf("%d", &A[i]);
             }
            注意这里的malloc是分配内存，所以这里数组A的内存是连续的
          二、python：

          三、高数：

          四、汇编：

          五、linux指令：
            

      



**自动创建时间：** Sat Dec 13 00:26:12 CST 2025
