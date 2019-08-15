#coding = utf-8

from selenium import webdriver      #从selenium中导入webdriver
from time import sleep



#使用自带的Safari浏览器

browser = webdriver.Safari()        #调用webdriver的Safari方法，打开safari浏览器
browser.get('http://www.baidu.com')     #get函数获取url地址，访问url

browser.get_screenshot_as_file('/Users/hufengge/Desktop/自动化截屏/首页.png') #截屏
print(browser.get_screenshot_as_base64())
sleep(3)
browser.quit()          #关闭浏览器

'''
#访问新的页面
browser = webdriver.Safari()
browser.get('http://news.baidu.com')


sleep(3)
browser.close()        #关闭所有页面。退出浏览器
'''


'''
browser.find_element(By.ID,'id1')
browser.find_element_by_id('id1')
browser.find_element_by_css_selector('#id1')

browser.find_element(By.CLASS_NAME,'class1')
browser.find_element_by_class_name('class1')
browser.find_element_by_css_selector('.class1')
'''

'''

#使用chrome浏览器

chromedriver='/usr/local/bin/ChromeDriver'             #需要添加驱动路径
browser = webdriver.Chrome(executable_path=chromedriver)
browser.get('http://wwww.baidu.com')
sleep(3)
browser.close()         #关闭当前页面
'''