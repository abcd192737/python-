# -*- coding: utf-8 -*-
"""
Created on Sat May 25 22:19:35 2019

@author: gingo
"""

from urllib.request import urlopen
from urllib.error import HTTPError

try:
    html = urlopen('http://pythonscaping.com/pages/page.html')
except HTTPError as e:#如果網站錯誤，將會印出HTTPError
    print(e)

  
    