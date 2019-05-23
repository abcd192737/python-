# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib.request as ur #使用python內建urllib函式庫
url='http://www.google.com'#使用Google來做測試
connection=ur.urlopen(url)
print(connection)
mydata=connection.read()
print(mydata)
print(connection.status)#網頁連接狀態
print(connection.getheader('Content-Type'))
for key,value in connection.getheaders():
    print(key,value)
