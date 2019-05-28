# -*- coding: utf-8 -*-
"""
Created on Tue May 28 23:13:45 2019

@author: gingo
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html,'lxml')

for sibling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sibling)