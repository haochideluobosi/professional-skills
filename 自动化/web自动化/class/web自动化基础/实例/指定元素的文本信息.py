#coding=utf-8
#检查元素是否被选中 is_selected,返回值为布尔值

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


#登陆帐号和密码输入空，点击登陆，查看报错信息
browser.find_element_by_id('lbNormal').click()

browser.switch_to.frame(0)
browser.find_element_by_id('dologin').click()

#显示等待
WebDriverWait(browser,5).until(expected_conditions.text_to_be_present_in_element((By.XPATH,'//div[contains(text(),"请输入帐号")]')))

browser.close()