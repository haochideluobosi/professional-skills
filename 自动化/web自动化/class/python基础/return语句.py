#coding=utf-8
def sum(arg1,arg2):
    total=arg1+arg2
    print(total)
    return total;

def area(width,length):
    "计算长方形的面积"
    return width*length;
#没有return 默认返回 return none

total=sum(1,2);

area=area(10,20)
print(area);
