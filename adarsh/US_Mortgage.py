# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:04:11 2018

@author: arvin
"""

from bs4 import BeautifulSoup as B
from urllib.request import Request, urlopen
req = Request('https://www.quora.com/search?q=US+Mortgage', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'})
page = urlopen(req).read()
soup = B(page, 'html.parser')
#print(soup)
res = soup.find_all('span', class_="question_text")
for i in res:
   #print(i.string)
   print(i.get_text())  #To get only the text

#questions = soup.find(class_='Question')