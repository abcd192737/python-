# -*- coding: utf-8 -*-
"""
Created on Tue May 28 23:08:28 2019

@author: gingo
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
 
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html,'lxml')

for child in bs.find('table',{'id':'giftList'}).children:#輸出子節點
    print(child)