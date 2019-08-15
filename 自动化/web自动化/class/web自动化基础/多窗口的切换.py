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

#点击注册链接
browser.find_element_by_xpath('//*[@id="commonOperation"]/a[2]').click()
sleep(2)
print(now_handle)  #认为还是在原窗口 (s2:来源页面）

#获取所有句柄
handles = browser.window_handles
print(handles)
for handle in handles:
    if handle != now_handle:
        browser.switch_to.window(handle)
        print(handle)
        sleep(2)
        browser.find_element_by_css_selector('#nameIpt').send_keys('hu18298378148')
        sleep(2)


browser.close()          #关闭浏览器








'''
browser.find_element(By.ID,'id1')
browser.find_element_by_id('id1')
browser.find_element_by_css_selector('#id1')

browser.find_element(By.CLASS_NAME,'class1')
browser.find_element_by_class_name('class1')
browser.find_element_by_css_selector('.class1')
'''