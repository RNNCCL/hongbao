# -*- coding: utf-8 -*-
from splinter.browser import Browser
import time
import traceback
from selenium import webdriver
import MySQLdb

ticket_url = "http://gsactivity.diditaxi.com.cn/gulfstream/activity/v2/giftpackage/index?g_channel=b870cd2164e4976223311eea14cb1bd8"
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
def getPhoneNumber():
    conn= MySQLdb.connect(host='localhost',port = 3306,user='root',db ='wool')
    cur=conn.cursor()
    cur.execute("select * from phone")
    phoneNumberList = cur.fetchall()  ## this is a tuple of tuple, to access the number, should use phoneNumberList[i][0]
    conn.close()
    cur.close()
    return phoneNumberList
if __name__ == "__main__":
    driver=webdriver.Chrome()
    filehandle=open('phone.txt','r')
    phoneNumberList= getPhoneNumber()
    for phoneNumber in phoneNumberList:
        print "hello times=====",phoneNumber
        didi(phoneNumber[0])
        time.sleep(5)
