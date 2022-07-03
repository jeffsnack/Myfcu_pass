#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
list1 = []
url = "https://myfcu.fcu.edu.tw/main/infomyfculogin.aspx"


driverPath =r'C:\Users\user\Downloads\chromedriver_win32 (4)\chromedriver.exe' #chromedriver的路徑位置
chrome = webdriver.Chrome(driverPath)
chrome.get(url)
username = chrome.find_element_by_id('txtUserName')
username.send_keys('')#輸入my_fcu帳號
password = chrome.find_element_by_id('txtPassword')
password.send_keys('')#輸入my_fcu密碼
ok_btn = chrome.find_element_by_id('OKButton')
ok_btn.click()

time.sleep(3)



chrome.get('https://myfcu.fcu.edu.tw/main/webClientMyFcuMain.aspx#/prog/SP3300016')
time.sleep(3)
chrome.switch_to.frame('main') #先進入iframe,才能定位到本頁的元素
time.sleep(3)

if chrome.find_element_by_xpath('/html/body/div[1]/div/div[1]/h4').text != 'PASS':
    close = chrome.find_element_by_xpath('/html/body/div[1]/div/div[3]/button')
    close.click()
    time.sleep(3)
    temp = chrome.find_element_by_xpath('//*[@id="form1"]/div[3]/div[3]/ng-form[2]/div/div/table/tbody/tr[3]/td/div/label[9]/input')
    temp.click()
    time.sleep(3)
    save = chrome.find_element_by_xpath('//*[@id="form1"]/div[3]/div[3]/ng-form[2]/div/div/table/tbody/tr[1]/th/div/input')
    save.click()
else:
    chrome.find_element_by_xpath('/html/body/div[1]/div/div[1]')
    date = chrome.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div[1]').text
    print(f'today is {date}')
    time.sleep(3)
    close = chrome.find_element_by_xpath('/html/body/div[1]/div/div[3]/button')
    close.click()

 


# In[ ]:




