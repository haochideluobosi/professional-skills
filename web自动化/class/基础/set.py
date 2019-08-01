#coding=utf-8

student={'tom','jim','mary'}
print(student)

#成员测试

if 'rose' in student:
    print('rose在集合中')

else:
    print("rose不在集合中")

#集合运算

a=set('abcd')
b=set('1234a')

print(a)
print(b)
print(a-b) #a和b的差集
print(b-a) #b和a的差集

print(a|b) #a和b的并集

print(a&b)#a和b的交集

print(a^b)#a和b不同时存在的元素