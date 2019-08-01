#coding=utf-8

total=0;#全局变量

def sum(arg1,arg2):
    total=arg1*arg2
    print(total)
    return total;

#调用函数
sum(10,20);
print(total); #调用全局变量

