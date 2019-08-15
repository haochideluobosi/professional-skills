#coding=utf-8

from selenium import  webdriver
from time import sleep

#启动浏览器
browser = webdriver.Safari()
browser.get('http://sso.yf.dasouche.net/login.htm?')
sleep (3)

#窗口最大化
browser.maximize_window()

#登陆
login_username=browser.find_element_by_id('username').send_keys('15310011102')
login_pw=browser.find_element_by_id('password').send_keys('aa123123')
sleep(2)

login_button=browser.find_element_by_id('submit-btn')
login_button.click()
sleep(10)



#点击一级功能菜单的客户

customerbtn=browser.find_element_by_xpath('//div[@class="first-level-title"]//a[contains(text(),"客户")]')       #根据父子节点结合包裹标签定位
customerbtn.click()
sleep(3)

#点击二级菜单的客户管理
custbtn=browser.find_element_by_xpath('//a[@href="https://dev.yf.dasouche.net/index.html?url=https://f2e.yf.dasouche.net/infiniti/new-customer-management/list.html"]').click()
sleep(10)



browser.close()