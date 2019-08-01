#coding = utf-8

from selenium import webdriver
from time import sleep

browser = webdriver.Safari()
first_url ='http://www.baidu.com'
browser.get(first_url)
sleep(3)

second_url = 'http://news.baidu.com'
browser.get(second_url)
sleep(3)

browser.back()          #后退
sleep(3)

browser.forward()       #前进
sleep(3)

browser.refresh()       #刷新当前页面
sleep(3)

print(browser.page_source)      #打印源码
sleep(3)

browser.quit()      #关闭浏览器所有页面，退出浏览器

