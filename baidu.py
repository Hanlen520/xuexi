""" 
@author: lileilei
@file: baidu.py 
@time: 2018/6/22 9:01 
"""
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
d=webdriver.Chrome()
d.get('http://www.baidu.com/')
d.find_element_by_xpath('//*[@id="u1"]/a[8]').click()
d.find_element_by_class_name('setpref').click()
time.sleep(6)
s1=Select(d.find_element_by_name("NR"))
d.find_element_by_class_name('prefpanelgo').click()
d.switch_to_alert().accept()