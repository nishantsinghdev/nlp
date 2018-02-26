# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:06:46 2018

@author: arvin
"""

#import validators
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys 

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--window-size=1920x1080")
chrome_driver = "C:\\Users\\arvin\\Downloads\\chromedriver_win32\\chromedriver.exe"

browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
# browser = webdriver.Chrome("C:\\Users\\arvin\\Downloads\\chromedriver_win32\\chromedriver.exe")
url='https://www.quora.com//search?q=US+Mortgage'
browser.get(url)

body=browser.find_element_by_tag_name('body')

for i in range(10):
   body.send_keys(Keys.PAGE_DOWN)
   time.sleep(0.5)

questions=browser.find_elements_by_class_name('question_link')
n=1
for question in questions:
   print(str(n)+".) "+question.text)
   print("Link : "+question.get_property('href'), end="\n\n")
   n += 1
   if n==11:
       break

browser.quit()