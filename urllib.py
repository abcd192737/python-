# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib.request as ur #使用python內建urllib函式庫
url='http://10.0.2.12'#使用Google來做測試
connection=ur.urlopen(url)#打開網頁
print(connection)#印出蒐集到的資料
mydata=connection.read()#讀取連接的資料並儲存於mydata
print(mydata)
print(connection.status)#status=網頁連接狀態
print(connection.getheader('Content-Type'))#取得標頭檔
for key,value in connection.getheaders():
    print(key,value)#印出迴圈
