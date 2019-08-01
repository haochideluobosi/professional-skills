#coding=utf-8

"""
格式：
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
"""

num=int(input("请输入一个数字"))
if num%2==0:
    if num%3 == 0:
        print("输入的数字可同时整除2和3")
    else:
        print("输入的数字可整除2，但不能整除3")
else:
    if num%3==0:
        print("输入的数字可整除3，但不能整除2")
    else:
        print("输入的数字既不能8整除2，也不能整除3")