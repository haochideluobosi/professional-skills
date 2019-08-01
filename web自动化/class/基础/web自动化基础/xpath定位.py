#coding=utf-8

from selenium import webdriver      #从selenium中导入webdriver
from time import  sleep

#打开浏览器
browser = webdriver.Safari()             #调用webdriver的Safari方法，打开safari浏览器
browser.get('http://www.baidu.com')     #get函数获取url地址，访问url
sleep(3)

#使用xpath定位到元素
'''
search=browser.find_element_by_id('kw').send_keys('1')   #用id定位
search = browser.find_element_by_xpath('//input[@id="kw"]').send_keys('考拉')      #选取属性满足id=kw的input元素
search=browser.find_element_by_xpath('//input[@name="wd"]').send_keys('考拉')         #选取属性name=wd的input元素

'''
search=browser.find_element_by_xpath('//input[@class="s_ipt"]').send_keys('考拉')     #选择属性class=s_ipt的input元素
button=browser.find_element_by_xpath('//input[@class="bg s_btn"]')     #选择属性class=s_ipt的input元素
button.click()

#level_1s = browser.find_elements_by_xpath('//div[@class="outCont"]//table[@class="table01"]//tr')

search=browser.find_elements_by_xpath('//div[@class="onCont"]//table[@class="table01"]//tr')
sleep(5)
browser.close()
