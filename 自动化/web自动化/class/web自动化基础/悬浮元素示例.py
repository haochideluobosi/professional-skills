# coding = utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

chromedriver = '/usr/local/bin/ChromeDriver'  # 需要添加驱动路径
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.implicitly_wait(30)
browser.get('http://www.baidu.com')

# 对ActionChains类进行实例化
actionChains = ActionChains(browser)
# print(browser.get_screenshot_as_base64())

# 鼠标悬停操作
#settingbtn = browser.find_element_by_css_selector('#u1 > a.pf')
settingbtn = browser.find_element_by_xpath('//*[@id="u1"]/a[8]')
actionChains.move_to_element(settingbtn).perform()
# sleep(10)

# searchsetting = browser.find_element_by_xpath('//div[@class="bdnuarrow"]//a[@class="class="setpref""]')
# sleep(2)
searchsetting=browser.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]')

# browser.get_screenshot_as_file('/Users/hufengge/Desktop/自动化截屏/悬停1.png')  # 截屏
searchsetting.click()

sleep(3)
browser.quit()
