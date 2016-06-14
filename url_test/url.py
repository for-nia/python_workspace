#!/usr/bin/python

import requests
import urlparse
from bs4 import BeautifulSoup

url='https://www.zhihu.com/question/19993706#answer-36386257'

response=requests.get(url,verify=False)
soup=BeautifulSoup(response.content,'html.parser')
a_tags=soup.find_all('a')
s=set()
for tag in a_tags:
    url_temp=urlparse.urljoin(url,tag.get('href'))
    if url_temp not in s:
        s.add(url_temp)
    else:
        print 'the set has contain the url %s'%url_temp
print '============================================'
for link in s:
    print link
