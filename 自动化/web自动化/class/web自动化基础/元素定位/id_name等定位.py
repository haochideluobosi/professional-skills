#coding=utf-8

from selenium import webdriver      #从selenium中导入webdriver
from time import  sleep

#打开浏览器
browser = webdriver.Safari()   #调用webdriver的Safari方法，打开safari浏览器
browser.maximize_window()
browser.get('http://www.baidu.com')     #get函数获取url地址，访问url
sleep(1)

'''
# 用id定位,需要id不是动态变化的，而且是唯一的
search=browser.find_element_by_id('kw').send_keys('1')


#通过name定位
search=browser.find_element_by_name('wd').send_keys('selenium')
sleep(1)


#通过class_name定位
browser.find_element_by_class_name('s_ipt').send_keys('selenium')
sleep(1)


#通过link_text定位,通常用来定位超链接,主要以a标签
browser.find_element_by_link_text('视频').click()
'''

#通过partial_link_text定位,也用于对超链接的处理，模糊搜索
browser.find_element_by_partial_link_text('频').click()  #太慢，弃用


browser.close()