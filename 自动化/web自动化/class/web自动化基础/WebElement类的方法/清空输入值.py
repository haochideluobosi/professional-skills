#coding=utf-8
#清空输入值clear()

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select


chromedriver = '/usr/local/bin/ChromeDriver'
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('http://sso.yf.dasouche.net/login.htm?')
sleep(2)


#检查登陆页面用户名输入框是否有默认文案：用户名/手机号码
username = browser.find_element_by_id('username')   #先定位到要检查的输入框
username.send_keys('15310011102')
#输入帐号后，值传到value中
print('输入帐号：{0}'.format(username.get_attribute('value')))

username.clear()
print('输入帐号：{0}'.format(username.get_attribute('value')))

browser.close()