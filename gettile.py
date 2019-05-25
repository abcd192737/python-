# -*- coding: utf-8 -*-
"""
Created on Sat May 25 22:48:06 2019

@author: gingo
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def gettitle(url):#定義gettitle函式，url為此函式的input
    try:
        html = urlopen(url)#開啟url
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(),'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title#如果沒錯誤即回傳title
#有title的測試
title = gettitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:#檢查是否有title可顯示
    print('沒東西啊')
else:
    print(title)
#沒有title的測試
title = gettitle('http://www.google.com')
if title == None:#檢查是否有title可顯示
    print('沒東西啊')
else:
    print(title)

        