#coding = utf-8
#webdriver通过获取当前句柄来识别窗口

from selenium import webdriver      #从selenium中导入webdriver
from time import sleep

#进入163邮箱首页
chromedriver='/usr/local/bin/ChromeDriver'             #需要添加驱动路径
browser = webdriver.Chrome(executable_path=chromedriver)

browser.get('https://mail.qq.com/cgi-bin/loginpage')
sleep(3)

#点击密码登陆
browser.find_element_by_xpath('//a[@id="switchAccountLogin"]').click()

#定位输入框，在iframe框架中
browser.switch_to.frame('login_frame')       #使用索引的方式，进入到frame框架
browser.find_element_by_xpath('//input[@class="inputstyle"]').send_keys('18298378148')
sleep(2)



browser.close()