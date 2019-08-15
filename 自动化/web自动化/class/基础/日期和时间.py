#coding=utf-8

import time; #引入time模块

ticks=time.time() #调用time模块的time函数
print("当前时间戳:",ticks);

#获取当前时间
localtime=time.localtime(time.time())
print("本地时间为：",localtime)