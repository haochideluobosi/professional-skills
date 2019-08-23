#coding = utf-8
#方法page_source获取地址

from selenium import webdriver      #从selenium中导入webdriver
from time import sleep

#进入163邮箱首页
chromedriver='/usr/local/bin/ChromeDriver'             #需要添加驱动路径
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://mail.163.com/')
sleep(3)



now_handle = browser.current_window_handle        #目前操作的窗口为now_handle
browser.find_element_by_link_text('注册新帐号').click()
handles = browser.window_handles

print(now_handle)
#获取当前页面的代码
print(browser.page_source)

#获取新窗口页面的代码
sleep(2)
print(handles)
for handle in handles:
    if handle !=now_handle:     #如果当前视觉看到的窗口不是操作的窗口时
        browser.switch_to.window(handle)
        print(browser.current_window_handle)
        print(browser.page_source)
browser.close()