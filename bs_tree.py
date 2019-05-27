# -*- coding: utf-8 -*-
"""
Created on Mon May 27 22:17:12 2019

@author: gingo
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.tibame.com')#robots.txt allow因此採用此網站
bs = BeautifulSoup(html.read(), html.parser)
tree = bs.find_all(bs.tag.subtag.anotherSubTag)
    for trees in tree:
        print(tree)
        