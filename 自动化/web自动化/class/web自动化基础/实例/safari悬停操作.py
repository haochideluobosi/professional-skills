#coding=utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Safari()

try:
    browser.maximize_window()
    browser.implicitly_wait(30)
    browser.get('http://www.baidu.com')

    sleep(2)


    #对ActionChains类实例化

    actionChains=ActionChains(browser)

    #悬停在设置按钮上
    setting = browser.find_element_by_xpath('//*[@id="u1"]/a[8]')
    actionChains.move_to_element(setting).perform()

    browser.get_screenshot_as_file('/Users/hufengge/Desktop/自动化截屏/safari设置悬停.png')

    #点击搜索设置
    browser.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()
    sleep(2)

    #点击空白区域
    #browser.find_element_by_xpath('//*[@id="head"]/div/div[1]').click()

    browser.find_element_by_xpath('//*[@id="se-setting-7"]/div[2]/a').click()
    sleep(2)
    browser.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__closeBtn"]').click()
    sleep(2)


    #悬停在设置按钮上，点击预测
    setting = browser.find_element_by_xpath('//*[@id="u1"]/a[8]')
    sleep(2)
    actionChains.move_to_element(setting).perform()
    sleep(2)

    browser.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[2]').click()
    sleep(2)



except Exception as e:
    e.with_traceback()
    pass
finally:
    browser.close()

