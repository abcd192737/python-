# -*- coding: utf-8 -*-
"""
Created on Sun May 26 11:45:30 2019

@author: gingo
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
#爬標籤下的資料
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.find_all('span' , {'class':'green'} )#找出所有擁有{'class':'green'}標籤的資料
for name in nameList:
    print(name.get_text())#get_text()抽出文件並只印出unicode
#url測試
try:
    html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')#測試url是否輸入錯誤
except HTTPError as e:
    print(e)
except URLError as e:
    print('這個連結沒東西啦，換個連結試試看吧!')#如果url錯誤即會顯示
else:
    print('你成功啦啦啦')#若沒以上兩個錯誤即會顯示
    