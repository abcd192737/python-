# -*- coding: utf-8 -*-
"""
Created on Sat May 25 22:02:53 2019

@author: gingo
"""

from urllib.request import urlopen#匯入urlopen函式
from bs4 import BeautifulSoup#匯入beautifulsoup函式

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')#呼叫html.read()取得網頁的內容
print(bs.h1)#回傳<h1>的資料