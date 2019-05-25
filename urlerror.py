# -*- coding: utf-8 -*-
"""
Created on Sat May 25 22:32:28 2019

@author: gingo
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError#url錯誤的函式

try:
    html = urlopen('http://pythonscraptingthisurldoesexist.com')#測試一個不存在的url
except HTTPError as e:
    print(e)
except URLError as e:
    print('這個連結沒東西啦，換個連結試試看吧!')#如果url錯誤即會顯示
else:
    print('你成功啦啦啦')#若沒以上兩個錯誤即會顯示
    
