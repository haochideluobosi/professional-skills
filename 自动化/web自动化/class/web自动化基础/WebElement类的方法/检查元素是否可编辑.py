#coding=utf-8
#检查元素是否可见 is_enabled,返回值为布尔值

from selenium import webdriver
from time import sleep


chromedriver = '/usr/local/bin/ChromeDriver'
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://mail.163.com')
sleep(2)

login_by_user=browser.find_element_by_id('lbNormal')
print('右上角密码登陆是否可编辑：{0}'.format(login_by_user.is_displayed()))
browser.close()