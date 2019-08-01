#coding=utf-8

from selenium import  webdriver
from time import sleep

#登陆
chromedriver='/usr/local/bin/ChromeDriver'             #需要添加驱动路径
browser = webdriver.Chrome(executable_path=chromedriver)
browser.get('https://sso.yf.dasouche.net/login.htm?')
sleep(3)

browser.maximize_window()


login_username=browser.find_element_by_id('username').send_keys('15310011102')
login_pw=browser.find_element_by_id('password').send_keys('aa123123')
sleep(2)

login_button=browser.find_element_by_id('submit-btn')
login_button.click()
sleep(10)


#点击进入订单管理



#点击进入客户管理

customerbtn=browser.find_element_by_xpath('//div[@class="first-level-title"]//a[contains(text(),"客户")]')       #根据父子节点结合包裹标签定位
customerbtn.click()
sleep(3)


custbtn=browser.find_element_by_xpath('//a[@href="https://dev.yf.dasouche.net/index.html?url=https://f2e.yf.dasouche.net/infiniti/new-customer-management/list.html"]').click()
sleep(10)


order=browser.find_element_by_xpath('//div[@class="first-level-title"]//a[contains(text(),"订单")]')
order.click()
sleep(3)

ordermanager=browser.find_element_by_xpath('//div[@class="second-level-title"]//a[contains(text(),"订单管理")]')
ordermanager.click()
sleep(10)


browser.close()