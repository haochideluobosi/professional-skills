#coding=utf-8


#有问题，未实现键盘操作

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

chromedriver = '/usr/local/bin/ChromeDriver'
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://www.baidu.com')


sou=browser.find_element_by_id('kw')
sou.send_keys('selenium')
WebDriverWait(browser,3)
#选中输入框内容
sou.send_keys(Keys.COMMAND,'a')
sleep(2)
#复制输入框内容
sou.send_keys(Keys.COMMAND,'c')

browser.find_element_by_xpath('//a[contains(text(),"百度首页")]').click()
browser.find_element_by_id('kw').send_keys(Keys.COMMAND,'v')
sleep(2)


browser.close()