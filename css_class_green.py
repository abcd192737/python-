# -*- coding: utf-8 -*-
"""
Created on Sun May 26 11:45:30 2019

@author: gingo
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.find_all('span' , {'class':'green'} )#找出所有擁有{'class':'green'}標籤的資料
for name in nameList:
    print(name.get_text())#get_text()抽出文件並只印出unicode
    