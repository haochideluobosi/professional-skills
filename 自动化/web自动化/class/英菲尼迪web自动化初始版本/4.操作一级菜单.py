# coding=utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# 启动
browser = webdriver.Safari()
browser.get('http://sso.yf.dasouche.net/login.htm?')
browser.maximize_window()
sleep(2)

# 登陆
login_username = browser.find_element_by_id('username').send_keys('15310011102')
login_pw = browser.find_element_by_id('password').send_keys('aa123123')
sleep(2)

login_button = browser.find_element_by_id('submit-btn')
login_button.click()
sleep(5)

#对ActionChains实例化
actionChains=ActionChains(browser)

# 客户管理
customerbtn = browser.find_element_by_xpath(
    '//div[@class="first-level-title"]//a[contains(text(),"客户")]')  # 根据父子节点结合包裹标签定位
customerbtn.click()
sleep(2)

# 点击二级菜单的客户管理
custbtn = browser.find_element_by_xpath(
    '//a[@href="https://dev.yf.dasouche.net/index.html?url=https://f2e.yf.dasouche.net/infiniti/new-customer-management/list.html"]').click()
sleep(3)

# 订单管理
order = browser.find_element_by_xpath('//div[@class="first-level-title"]//a[contains(text(),"订单")]')
order.click()
sleep(2)

ordermanager = browser.find_element_by_xpath('//div[@class="second-level-title"]//a[contains(text(),"订单管理")]')
ordermanager.click()
sleep(3)

# 点击进入销售工具

# 1.销售工具-报价单管理-金融方案管理
saletool = browser.find_element_by_xpath('//div[@class="first-level-title"]//a[contains(text(),"销售工具")]')
saletool.click()
sleep(2)

financial = browser.find_element_by_xpath("//a[contains(text(),'报价单管理')]")
financial.click()
sleep(2)

financialplan = browser.find_element_by_xpath(
    '//a[@href="https://dev.yf.dasouche.net/index.html?url=https://f2e.yf.dasouche.net/infiniti/infiniti-quotation-pc/#/"]')
financialplan.click()
sleep(5)

#2.销售工具-报价单管理-报价项设置
saletool = browser.find_element_by_xpath('//div[@class="first-level-title"]//a[contains(text(),"销售工具")]').click()
sleep(2)

financial=browser.find_element_by_xpath("//a[contains(text(),'报价单管理')]").click()
sleep(2)

financial_configure = browser.find_element_by_xpath('//a[@href="https://dev.yf.dasouche.net/index.html?url=https://f2e.yf.dasouche.net/infiniti/infiniti-quotation-pc/#/quotation-items-setting"]')
financial_configure.click()
sleep(5)

#3.销售工具-交车管理-交车感谢函
saletool=browser.find_element_by_xpath('//a[contains(text(),"销售工具")]').click()
pickcar=browser.find_element_by_xpath('//ul[@class="second-level"]//a[contains(text(),"交车管理")]').click()
thanksletter = browser.find_element_by_xpath('//a[@href="https://dev.yf.dasouche.net/index.html?url=https://f2e.yf.dasouche.net/infiniti/icar-thanksLetter-editor/#/"]')
thanksletter.click()

#4.销售工具-交车管理-车型功能管理
saletool=browser.find_element_by_xpath('//a[contains(text(),"销售工具")]').click()
pickcar=browser.find_element_by_xpath('//ul[@class="second-level"]//a[contains(text(),"交车管理")]').click()
car = browser.find_element_by_xpath('//a[@href="https://dev.yf.dasouche.net/index.html?url=https://f2e.yf.dasouche.net/infiniti/icar_trade_pc/carModelFuncManage.html"]').click()

#5.销售工具-交车管理-功能库
saletool=browser.find_element_by_xpath('//a[contains(text(),"销售工具")]').click()
pickcar=browser.find_element_by_xpath('//ul[@class="second-level"]//a[contains(text(),"交车管理")]').click()
car = browser.find_element_by_xpath('//a[@href="https://dev.yf.dasouche.net/index.html?url=https://f2e.yf.dasouche.net/infiniti/icar_trade_pc/functionLibrary.html#/"]').click()


#6.销售工具-交车管理-视频库
saletool=browser.find_element_by_xpath('//a[contains(text(),"销售工具")]').click()
pickcar=browser.find_element_by_xpath('//ul[@class="second-level"]//a[contains(text(),"交车管理")]').click()
car = browser.find_element_by_xpath('//a[@href="https://dev.yf.dasouche.net/index.html?url=https://f2e.yf.dasouche.net/infiniti/icar_trade_pc/video.html"]').click()

#7.销售工具-试驾协议模版
saletool=browser.find_element_by_xpath('//a[contains(text(),"销售工具")]').click()
entract=browser.find_element_by_xpath('//a[@href="https://dev.yf.dasouche.net/index.html?url=https://f2e.yf.dasouche.net/sales-contract-printing/#/"]').click()

#8.销售工具-销售学院
actionsChains=ActionChains(browser)


saletool=browser.find_element_by_xpath('//a[contains(text(),"销售工具")]')
actionsChains.move_to_element(saletool).perform()
sleep(2)

saleschool=browser.find_element_by_xpath('//ul[@class="second-level"]//a[@href="https://dev.yf.dasouche.net/index.html?url=https://saler-school.yf.dasouche.net/articleList.html"]').click()


browser.close()
