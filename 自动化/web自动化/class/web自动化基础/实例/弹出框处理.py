#coding=utf-8
#webdriver的Alert类处理弹出框

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from time import sleep



chromedriver = '/usr/local/bin/ChromeDriver'
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://www.baidu.com')
sleep(2)

#悬浮到设置上并点击搜索设置
actionchains = ActionChains(browser)
setting = browser.find_element_by_link_text('设置')
actionchains.move_to_element(setting).perform()

browser.find_element_by_xpath('//a[@class="setpref"]').click()
sleep(2)

#点击保存设置
browser.find_element_by_link_text('保存设置').click()
sleep(2)



#处理alert框---获取弹框文案
message=browser.switch_to.alert.text            #获取alert文本信息
print('弹框提示文案：',message)
#print('弹框提示文案：{0}'.format(browser.switch_to.alert.text))
browser.switch_to.alert.accept()        #确认操作
#browser.switch_to.alert.dismiss #取消操作
#browser.switch_to.alert.send_keys('aaa')   #输入内容


'''
#启动登陆
chromedriver = '/usr/local/bin/ChromeDriver'
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://sso.yf.dasouche.net/login.htm？')
sleep(2)

browser.find_element_by_id('username').send_keys('15310011102')
browser.find_element_by_id('password').send_keys('aa123123')
browser.find_element_by_id('submit-btn').click()

#悬浮元素进入到需要页面
actionsChanins = ActionChains(browser)

saletool = browser.find_element_by_xpath('//div[@class="first-level-title"]//a[contains(text(),"销售工具")]')
actionsChanins.move_to_element(saletool).perform()
sleep(2)

financial=browser.find_element_by_xpath('//a[contains(text(),"报价单管理")]')
actionsChanins.move_to_element(financial).perform()
browser.find_element_by_link_text('报价项设置').click()
sleep(3)

#定位元素
browser.switch_to.frame(0)
browser.find_element_by_xpath('//button[@class="so-button so-button--primary"]').click()
sleep(3)

browser.find_element_by_xpath('//button[@class="so-button"]').click()
sleep(3)

#处理alert弹框--点击弹框取消
#browser.switch_to.alert.dismiss()   #例子不是alert，泪奔。。。，语法没错，不找例子了
browser.find_element_by_xpath('//button[@class="so-button so-button--small"]').click()
browser.switch_to.default_content()
'''
browser.close()



