#coding=utf-8



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

chromedriver = '/usr/local/bin/ChromeDriver'
browser = webdriver.Chrome(executable_path=chromedriver)
browser.maximize_window()
browser.get('https://www.baidu.com')
browser.find_element_by_id('kw').send_keys('selenium')
browser.find_element_by_id('su').click()



#滑动到任意位置  通过改变scrollTop的值
js='var q=document.documentElement.scrollTop=5000'
sleep(3)
browser.execute_script(js)
sleep(2)

#滑动到顶部
up='var q=document.documentElement.scrollTop=0'
sleep(3)
browser.execute_script(up)
sleep(2)

#将滚动条滑动到页面底部
down='var q=document.documentElement.scrollTop=100000'  #1000，不能滑动
sleep(3)        #不等待的话，不会报错，但是不滑动。滚动条还未加载出来
browser.execute_script(down)
sleep(3)


#点击下一页
browser.find_element_by_link_text('下一页>').click()   #这里文本有>符号
sleep(2)



browser.close()
