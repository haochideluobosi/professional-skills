#coding=utf-8
#context_click()鼠标右键操作



from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

chromedriver = '/usr/local/bin/ChromeDriver'
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://mail.163.com')
sleep(2)

actionschains=ActionChains(browser)
pw_login=browser.find_element_by_id('switchAccountLogin')
actionschains.double_click(pw_login)

browser.close()