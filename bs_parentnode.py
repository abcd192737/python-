# -*- coding: utf-8 -*-
"""
Created on Tue May 28 23:18:23 2019

@author: gingo
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html,'lxml')
print(bs.find('img',{'src':'.../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
