#coding = utf-8


from selenium import webdriver      #从selenium中导入webdriver
from time import sleep

#进入163邮箱首页
chromedriver='/usr/local/bin/ChromeDriver'             #需要添加驱动路径
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://www.baidu.com/')
sleep(3)

#定位百度首页输入框
#1.by_tag_name
tag_names=browser.find_elements_by_tag_name('input')
for tag_name in tag_names:
    print (tag_name)
    print (type(tag_names))

#输入框位于标签中的第8位，即索引中的第7位
browser.find_elements_by_tag_name('input')[7].send_keys('selenium')
#或者写成 tag_names[7].send_keys('selenium')
sleep(2)
browser.close()

#2.find_elements_by_id 思路同上，暂未找到例子

#3.其他定位方式同上