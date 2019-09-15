#coding=utf-8



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


def richText(content):
    '''往富文本里输入内容'''
    js="document.getElementByClass('APP-editor-iframe').contentWindow."\
        "document.body.innerHTML='[0]'".format(content)
    browser.execute_script(js)

#登陆进入系统

chromedriver='/usr/local/bin/ChromeDriver'             #需要添加驱动路径
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://mail.163.com')
sleep(2)

#操作右上角选择密码登陆方式
browser.find_element_by_xpath('//a[@id="switchAccountLogin"]').click()

#定位到iframe页面
browser.switch_to.frame(0)       #使用索引的方式，进入到frame框架
browser.find_element_by_xpath('//input[@name="email"]').send_keys('18298378148')
browser.find_element_by_xpath('//input[@name="password"]').send_keys('hfg11250323')
browser.find_element_by_id('dologin').click()

browser.switch_to.default_content()     #跳出frame框架
sleep(2)

#点击写信
browser.find_element_by_id('_mail_component_24_24').click()



'''
#进入iframe
browser.switch_to.frame(0)
browser.find_element_by_xpath('//body[@class="nui-scroll"]')
'''


richText('python自动化测试输入文本')
sleep(2)


browser.close()

















