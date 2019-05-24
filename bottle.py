# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#使用Bottle
from bottle import run,static_file,route

@route('/')#將網頁路由到根目錄
def www():
    return static_file('index.html',root='.')#放置於根目錄
#執行
run(host='localhost',port=9999)#連接埠設為9999
