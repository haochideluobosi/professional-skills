#coding=utf-8

str='python'
print(str)

#字符串的截取,正向从0开始，反向从-1开始

print(str[1])  #输出字符串第二个字符

print(str[-1])#输出字符串到倒数第二个字符

print(str[2:-1])#输出第三个到最后一个字符

print(str[3:])#输出

#字符串连接

print(str+'mysql') #字符串拼接
print('mysql'+str)
#print(mysql+str)  #未使用引号报错


print(str*3)#字符串重复3次


#字符串转义
print('pyt\nhon') #使用\n转义字符串
print(r'pyt\nhon')#使用r不让反斜杠发生转义

