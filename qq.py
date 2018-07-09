""" 
@author: lileilei
@file: qq.py 
@time: 2018/6/22 11:12 
"""
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['preformVersion'] = '4.4.2'
desired_caps['appPackage'] = 'com.tencent.mobileqq'
desired_caps['appActivity'] = '.activity.SplashActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(10)
TouchAction(driver).press(x=2,y=235).wait(1000).move_to(x=250,y=235).release().perform()
driver.find_element_by_id('com.tencent.mobileqq:id/nickname').click()
