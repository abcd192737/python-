# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:46:29 2019

@author: gingo
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html,'html.parser')
for tree in bs.tag.subTag.anotherSubTag:
    print(tree.get_text())
    
try:
    badContent = bs.nonExistingTag.anotherTag
except AttributeError as e:
    print('Tag was not found')
else:
    if badContent == None:
        print('Tag was not found')
    else:
        print(badContent)