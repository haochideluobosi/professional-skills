#coding=utf-8


#定义函数
def printme(str):
    "打印任何传入的字符串"
    #print str; print 输入后面需要加（），否则报错
    print(str);
    return;

def printinfo(name,age=35):
    '打印输入的姓名，年龄'
    print(name);
    print(age);

def printinfo1(arg1,*vartuple):#不定长参数
    '打印任何传入的参数'
    print(arg1)
    for var in vartuple:
        print(var)
    return;

def changeint(a):
    a=9
    return;

def change(mylisy):
    "打印输入的列表"
    mylist.append([1,2,3,4])
    return;



#调用函数
printme("python");
printme("再调一次");
printinfo(age=10, name='python');  #关键字参数，顺序可不对应，根据关键字自动匹配
printinfo(name='mike'); #age未传入，使用默认参数
printinfo1(10); #printinfo1为不定长参数
printinfo1(11,'yu',12);

#传不可变参数
b=9
changeint(b)
print(b);

#传递可变参数
mylist=[10,20,30]
change(mylist)
print("函数外取值：",mylist);


printme();   #必备参数，为空会报错


#参数类型；必备参数/关键字参数/默认参数/不定长参数
