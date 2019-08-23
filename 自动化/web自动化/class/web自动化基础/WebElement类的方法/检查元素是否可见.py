#coding=utf-8
#检查元素是否可见 is_displayed,返回值为布尔值

from selenium import webdriver
from time import sleep


chromedriver = '/usr/local/bin/ChromeDriver'
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://mail.163.com')
sleep(2)

login_byuser=browser.find_element_by_id('lbNormal')
print('右上角密码登陆按钮是否可见：{0}'.format(login_byuser.is_displayed()))
browser.close()
