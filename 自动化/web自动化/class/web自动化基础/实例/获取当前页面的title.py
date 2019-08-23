#coding=utf-8
#获取方法 title()

from selenium import webdriver
from time import sleep


chromedriver = '/usr/local/bin/ChromeDriver'
browser = webdriver.Chrome(executable_path=chromedriver)
browser.get('https://mail.163.com/')
browser.maximize_window()
sleep(2)


now_handle=browser.current_window_handle    #主窗口
browser.find_element_by_link_text('注册新帐号').click()      #操作后会打开子窗口
handles=browser.window_handles
print(now_handle)
print(handles)

for handle in handles:
    if handle != now_handle:    #当前呈现的窗口不是操作的窗口时
        print(browser.title)
        browser.switch_to.window(handle)
        print(handle)
        print(browser.title)
        browser.close()
#切回到主窗口
browser.switch_to.window(now_handle)
print(now_handle)


print('测试执行的浏览器为：{0}'.format(browser.name))     #获取执行的浏览器名称
browser.close()
