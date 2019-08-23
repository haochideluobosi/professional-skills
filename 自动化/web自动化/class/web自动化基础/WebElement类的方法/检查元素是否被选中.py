#coding=utf-8
#检查元素是否被选中 is_selected,返回值为布尔值

from selenium import webdriver
from time import sleep


chromedriver = '/usr/local/bin/ChromeDriver'
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://mail.163.com')
sleep(2)

login_by_user=browser.find_element_by_id('lbNormal').click()

#检查【十天内免登录】是否默认被选中
browser.switch_to.frame(0)
box = browser.find_element_by_id('un-login')
print('十天内免登陆是否默认被选中：{0}'.format(box.is_selected()))

#选中中查看是否被选中
box.click()
print('十天内免登陆选中状态：{0}'.format(box.is_selected()))

browser.close()