#coding=utf-8
#text_to_be_present_in_element用来判断元素中是否存在指定文本


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
browser.find_element_by_name('email').send_keys('')
browser.find_element_by_name('password').send_keys('')
browser.find_element_by_id('dologin').click()



#显示等待+判断元素是否存在指定文本--返回结果ture
result=WebDriverWait(browser,5).until(expected_conditions.text_to_be_present_in_element((By.XPATH,'//div[contains(text(),"请输入帐号")]'),'请输入帐号'))
print('是否包含文本信息：',result)

'''
#显示等待+判断元素是否存在指定文本--返回结果不符合预期时
result=WebDriverWait(browser,5).until(expected_conditions.text_to_be_present_in_element((By.XPATH,'//div[contains(text(),"请输入帐号")]'),'请输入帐号呀'))
print('是否包含文本信息：',result)
'''
browser.close()