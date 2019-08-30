#coding=utf-8
#visibility_of_element_located 判断元素是否可见，定位到返回元素，定位不到元素报错

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep

chromedriver = '/usr/local/bin/ChromeDriver'
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://mail.163.com')
sleep(2)

#执行通过，返回元素
result = WebDriverWait(browser,5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,'注册新帐号')))   #后跟一个参数，用()扩起来
print(result)

'''
#执行不通过，显示等待+报错
result = WebDriverWait(browser,5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,'注册新帐号1')))   #后跟一个参数，用()扩起来
print(result)
'''
browser.close()







