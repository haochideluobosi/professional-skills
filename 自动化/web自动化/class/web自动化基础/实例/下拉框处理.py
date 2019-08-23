#coding=utf-8
#检查元素是否被选中 is_selected,返回值为布尔值

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select


chromedriver = '/usr/local/bin/ChromeDriver'
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://reg.mail.163.com/unireg/call.do?cmd=register.entrance&from=163mail_right')
sleep(2)

'''
#1.使用索引定位

#定位Select下拉框
email=browser.find_element_by_id('mainDomainSelect')
#实例化Select类
select = Select(email)
#索引定位下拉框选项中的值
select.select_by_index(1)
#查看当前下拉框的值
print('下拉框选项为：',email.get_attribute('value'))



#2.使用value值定位
email=browser.find_element_by_name('mainDomain')
select=Select(email)
select.select_by_value('yeah.net')
print('下拉框选项为：',email.get_attribute('value'))

sleep(1)
'''

#3.使用文本定位
email = browser.find_element_by_name('mainDomain')
select = Select(email)
select.select_by_visible_text('126.com')
print('下拉框选项为：',email.get_attribute('value'))
sleep(1)

browser.close()