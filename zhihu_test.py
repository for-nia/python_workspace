#!/usr/bin/python
# encoding UTF-8
import requests
import re
import time
headers_base = {

		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, sdch',
		'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
		'Connection': 'keep-alive',
		'Host': 'www.zhihu.com',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36', 
		'Referer': 'http://www.zhihu.com/',
		}
url='http://www.zhihu.com'
login_data={

		'email':'663693083@qq.com',
		'password':'year1234.',
		'remember_me':'true'
		        }
pattern=re.compile(r'name=\"_xsrf\".*value=\"(\w+)\"')
session=requests.session()
response=session.get(url,headers=headers_base)
content=response.content
xsrf=re.search(pattern,content)
print xsrf.group(1)
