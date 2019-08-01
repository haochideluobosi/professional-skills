#coding=utf-8

tuple=('abcd',123,12.9)
tuple2=('python',456)


print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple2*2)
print(tuple+tuple2)


#元组中的元素不可被修改
 tuple[0]=1
 print(tuple)
