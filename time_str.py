#!/usr/bin/python

import time
import requests
url='http://www.zhihu.com/captcha.gif?r=%d&type-login&lang=cn'%(time.time()*1000)
print url 
session=requests.session()
rep=session.get(url,stream=True)
f=open('captcha.gif','wb')
f.write(rep.content)

