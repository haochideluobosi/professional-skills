#coding = utf-8
#方法current_url 获取地址

from selenium import webdriver      #从selenium中导入webdriver
from time import sleep

#进入163邮箱首页
chromedriver='/usr/local/bin/ChromeDriver'             #需要添加驱动路径
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://mail.163.com/')
sleep(3)



browser.find_element_by_link_text(u'注册新帐号').click()
#获取地址
print(browser.current_url)  #原窗口地址
print(browser.current_window_handle)

#获取新窗口打开的地址
now_handle=browser.current_window_handle    #当前操作的窗口
handles=browser.window_handles
print (handles)
for handle in handles:
    if handle != now_handle:
        browser.switch_to.window(handle)
        print(browser.current_url)
        print(browser.current_window_handle)


browser.close()