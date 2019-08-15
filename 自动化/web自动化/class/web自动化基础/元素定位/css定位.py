#coding=utf-8

from selenium import webdriver      #从selenium中导入webdriver
from time import  sleep

browser = webdriver.Safari() #调用webdriver的Safari方法，打开safari浏览器
browser.maximize_window()
browser.get('http://www.baidu.com')     #get函数获取url地址，访问url
sleep(3)


#css定位

browser.find_element_by_css_selector('#kw').send_keys('selenium')   #  （#表示id属性）
'''
browser.find_element_by_css_selector('.s_ipt').send_keys('selenium')     #  （.表示class属性）

browser.find_element_by_css_selector('[name="wd"]').send_keys('selenium')     #使用name通过css定位

browser.find_element_by_css_selector('[maxlength="255"]').send_keys('selenium')
'''

sleep(2)
browser.close()
