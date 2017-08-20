#-*- coding:utf-8 -*-
#定位的方式：class_name,id,accessibilityid,xpath,android_uiautomator
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
dic = {}
#desired_caps['address'] = '127.0.0.1
dic["platformName"] = "Android"
dic['platformVersion'] = '4.4.2'
#dic['automationName'] = 'Appium'
dic['deviceName'] = '192.168.240.101:5555'
dic['appPackage'] = 'com.aetos'
dic['appActivity'] = 'com.aetos.ui.module.core.LoadingActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', dic)
sleep(5)
driver.find_element_by_id("com.aetos:id/login_user_et_account").clear()
driver.find_element_by_id("com.aetos:id/login_user_et_password").clear()
driver.find_element_by_id("com.aetos:id/login_user_et_account").send_keys("15623146075")
sleep(5)
driver.find_element_by_id("com.aetos:id/login_user_et_password").send_keys("wang636393")
sleep(5)
driver.find_element_by_id("login_btn").click()
sleep(10)











