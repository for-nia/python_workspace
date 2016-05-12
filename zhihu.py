#!/usr/bin/python
import requests
import re

response=requests.get('http://www.zhihu.com')
content=response.content
pattern=re.compile(r'name=\"_xsrf\".*value=\"(\w+)\"')
src_partern=re.compile(r'img.*class=\"Captcha-image\".*src=\"()\"')
xsrf=re.search(pattern,content)
validatesrc=re.search(src_partern,content)
if xsrf:
	print xsrf.group(1)
else:
	print 'no result'

if validatesrc:
	print validatesrc.group(1)
else:
	print 'no validate'
