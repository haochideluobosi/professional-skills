#coding = utf-8
#webdriver通过获取当前句柄来识别窗口

from selenium import webdriver      #从selenium中导入webdriver
from time import sleep

#进入163邮箱首页
chromedriver='/usr/local/bin/ChromeDriver'             #需要添加驱动路径
browser = webdriver.Chrome(executable_path=chromedriver)
browser.get('https://mail.163.com')
sleep(3)


#获取当前窗口句柄
now_handle = browser.current_window_handle
print(now_handle)
sleep(2)

#点击密码登陆导致页面变化
browser.find_element_by_xpath('//*[@id="switchAccountLogin"]').click()
sleep(2)

#查看是否产生新的句柄
handles = browser.window_handles
print(handles)


#点击输入账号
browser.find_element_by_class_name('j-inputtext dlemail j-nameforslide').send_keys('18298378148')
sleep(2)

browser.close()
