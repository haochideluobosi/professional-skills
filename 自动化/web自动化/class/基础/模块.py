#coding=utf-8

#直接import引入模块
#1.引入内置模块

import sys
import time
print("命令行参数如下：")
for i in sys.argv:
    print(i)

print(sys.getdefaultencoding()) #获取当前的编码格式
print("python路径为：","\n",sys.path)


"""2.引入自定义模块
# 斐波那契(fibonacci)数列模块
def fib(n):
    a,b=0,1
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
    print()

def fib2(n):
    result= []
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result
"""
#2.from ...import

#dir()函数，找到模块内定义的所有名称

