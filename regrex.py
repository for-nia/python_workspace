#!/usr/bin/python
# encoding: UTF-8
import re

s='''<input type="hidden" name="_xsrf" value="2a525424b5ccae2ec4426f67cee029cc">'''
src='''<img class="Captcha-image" alt="验证码" style="display: block;" src="/captcha.gif?r=1462979552059&type=login&lang=cn">'''

p=re.compile(r'name=\"_xsrf.*value=\"(\w+)\"')
srcp=re.compile(r'class=\"Captcha-image\".*src=\"([\w|&]+)\"')
r=re.search(p,s)
v=re.search(srcp,src)
if r:
	print r.group(1)
else:
	print 'no result'
	
if v:
	print v.group(1)
else:
	print 'no validate'

