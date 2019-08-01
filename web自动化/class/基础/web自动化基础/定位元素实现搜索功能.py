#coding=utf-8

from selenium import webdriver      #从selenium中导入webdriver
from time import  sleep

browser = webdriver.Safari()        #调用webdriver的Safari方法，打开safari浏览器
browser.get('http://www.baidu.com')     #get函数获取url地址，访问url
sleep(3)

#safari使用右键加检查元素标记显示

inputbox=browser.find_element_by_id('kw')        #通过id去定位元素

sleep(2)

inputbox=browser.find_element_by_id('kw').send_keys('陈情令')
sleep(3)

search=browser.find_element_by_id('su')

search.click()

sleep(3)

browser.quit()