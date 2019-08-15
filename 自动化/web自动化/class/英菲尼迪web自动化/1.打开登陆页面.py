#coding = utf-8

from selenium import webdriver
from time import sleep

browser = webdriver.Safari()
browser.get ('http://sso.yf.dasouche.net/login.htm?')
sleep(3)

login_username=browser.find_element_by_id('username').send_keys('15310011102')
sleep(2)

login_password=browser.find_element_by_id('password').send_keys('aa123123')
sleep(2)

loginbutton=browser.find_element_by_id('submit-btn')
sleep(2)


loginbutton.click()

sleep(2)

browser.quit()

