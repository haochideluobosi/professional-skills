#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep



chromedriver = '/usr/local/bin/ChromeDriver'
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://www.baidu.com')

#隐式等待30秒
browser.implicitly_wait(30)

inputs=WebDriverWait(browser,10).until(expected_conditions.element_to_be_clickable((By.ID,"kw")))
#在10秒范围内只要元素加载出来就可以输入关键字
#显示等待了10秒，调用静态方法until,又调用了element_to_be_clickable类
inputs.send_keys('selenium')


browser.close()

