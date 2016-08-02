#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import re
import time
import Image
headers_base = {
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'en,zh-CN;q=0.8,zh;q=0.6',
	'Connection':'keep-alive',
	'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	'Host':'www.zhihu.com',
	'Origin':'https://www.zhihu.com',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
	'X-Requested-With':'XMLHttpRequest'
	}
url='https://www.zhihu.com'
login_data={
        'email':'663693083@qq.com',
        'password':'year1234.',
        'remember_me':'true',
	#	'captcha_type':'cn'
        }
pattern=re.compile(r'name=\"_xsrf\".*value=\"(\w+)\"')
session=requests.session()
response=session.get(url,headers=headers_base,verify=False)
content=response.content
xsrf=re.search(pattern,content)
login_data['_xsrf']=xsrf.group(1).encode('utf-8')
print xsrf.group(1)
capcha_url='https://www.zhihu.com/captcha.gif?r=%d&type=login'%(time.time()*1000)
print capcha_url
capcha=session.get(capcha_url,headers=headers_base,stream=True,verify=False)
f=open('capcha.gif','wb')
f.write(capcha.content)
f.close()
#captcha={
#		'img_size':[200,44]
#		}
#input_points=[]
#print u'please input validate code'
#capcha_str=raw_input()
#input_list=re.split(r' ',capcha_str)
#for input_str in input_list:
#	input_points.append(re.split(r',',input_str))
#captcha['input_points']=input_points
#login_data['captcha']=captcha
#print login_data
image=Image.open('capcha.gif')
print image.size
h,w = image.size
small_image=image.resize((h/2,w/2))
pil=small_image.load()
for i in range(w/2):
    for j in range(h/2):
        v=pil[j,i]
        if v==0:
            print '?',
        else:
            print '.',
    print '\n'

print u'请输入验证码'
capcha_input=raw_input()
login_data['captcha']=capcha_input
url_login='https://www.zhihu.com/login/email'
rep=session.post(url_login,data=login_data,headers=headers_base,verify=False)
print rep.status_code
print rep.content
mcookies=rep.cookies
my_url='https://www.zhihu.com/'
session.cookies=mcookies
my_rep=session.get(my_url,headers=headers_base,verify=False)
#print my_rep.content
f_content=open('zhihu.html','wb')
f_content.write(my_rep.content)
f_content.close()
