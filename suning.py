# -*- coding: utf-8 -*-
from splinter.browser import Browser
import time
import traceback
from selenium import webdriver

ticket_url = "http://act.suning.com/act-wap-web/wap/differentred/index-sdsxf.do"
global driver

def didi(phonenumber):
    driver.get(ticket_url)
    try:
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys(phonenumber)
        #time.sleep(1)
        driver.find_element_by_id("submit").click()
        #time.sleep(4)
    except Exception as e:
        print(traceback.print_exc())

if __name__ == "__main__":
    driver=webdriver.Chrome()
    filehandle=open('phone.txt','r')
    for line in filehandle:
        print "hello times=====",line
        didi(line)
        time.sleep(5)
