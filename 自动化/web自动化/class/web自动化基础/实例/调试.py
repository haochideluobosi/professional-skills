#coding=utf-8
#检查元素是否被选中 is_selected,返回值为布尔值

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from time import sleep

chromedriver = '/usr/local/bin/ChromeDriver'
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://www.baidu.com')

'''
actionschains=ActionChains(browser)

more_products=browser.find_element_by_xpath('//a[contains(text(),更多产品)]')
actionschains.move_to_element(more_products).perform()
sleep(2)
'''

locator=browser.find_element_by_link_text('贴吧')
text=u'贴吧'
result = expected_conditions.text_to_be_present_in_element(locator,text)(browser)
print(result)

browser.close()







