#coding=utf-8
"""
python循环语句有 for 循环和  while语句

for语句格式：
for variable in sequence:
    statements
else:
    statements


while语句格式：

while 判断条件：
    语句
"""
#实例1
languages=['c','c++','perl','python']
for x in languages:
    print(x)


#实例1
sites=['baidu','goole','rubbo','taobao']
for site in sites:
    if site=='rubbo':
        print('循环数据' +site)
        break
    else:
        print('没有循环数据')
print("完成循环")


#range函数,内置函数，可生成数列
for i in range(5):
    print(i)
#使用range函数创建一个列表
print(list(range(5)))


#break语句跳出for循环
"""
for letter in 'python': #letter:字母
    if letter =='h':
        print("当前字母为：", letter)
        break
"""

for letter in 'python':#letter:字母
    if letter =='t':
        break
    else:
        print("当前字母：",letter)


#while
var =6
while var>5:
    print("当前变量值为：",var)
    var=var -1
    if var ==5:
        continue
    print("当前var值：",var) #相当于 else: print()







