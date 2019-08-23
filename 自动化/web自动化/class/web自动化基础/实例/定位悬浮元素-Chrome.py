#conding=utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
#悬停到元素上需要用到ActionChains类

#启动浏览器
chromedriver='/usr/local/bin/ChromeDriver'
browser=webdriver.Chrome(chromedriver)
browser.maximize_window()
browser.get("http://wwww.baidu.com")
sleep(2)


#对ActionChains类进行实例化
actionChains = ActionChains(browser)

#定位设置元素并悬停
setting = browser.find_element_by_xpath('//*[@id="u1"]/a[8]')
actionChains.move_to_element(setting).perform()
browser.get_screenshot_as_file('/Users/hufengge/Desktop/自动化截屏/设置悬停.png')

browser.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()

sleep(2)

#点击登录区域
browser.find_element_by_xpath('//*[@id="se-setting-7"]/div[2]/a').click()
sleep(2)

browser.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__closeBtn"]').click()
sleep(2)
browser.get_screenshot_as_file('/Users/hufengge/Desktop/自动化截屏/扫码登录.png')


#悬停在设置按钮上，点击关闭预测
setting = browser.find_element_by_xpath('//*[@id="u1"]/a[8]')

actionChains.move_to_element(setting).perform()

browser.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[2]').click()
#browser.get_screenshot_as_file('/Users/hufengge/Desktop/自动化截屏/关闭预测.png')




browser.close()
