# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:50:19 2018

@author: arvin
"""

#import requests
from bs4 import BeautifulSoup as B
from urllib.request import Request, urlopen
req = Request('https://www.quora.com/topic/Q-A-Websites', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()
soup = B(page, 'html.parser')

res = soup.find_all('span', class_="rendered_qtext")
for i in res:
    print(i.string)
    #print(i.get_text()) To get only the text


#def get_data(url, target, id_type, id_val)



#questions = soup.find(class_='Question')
#Q = questions.find_all('span').get_text()

#for question_text in Q:
    #print(Q.prettify())
