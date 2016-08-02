#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import re
import time
import Image
import loginData
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance
class GetSession(Singleton):
    def  __init__(self):
            headers_base = loginData.headers_base
            url='https://www.zhihu.com'
            login_data=loginData.login_data
            print headers_base
            print login_data
            pattern=re.compile(r'name=\"_xsrf\".*value=\"(\w+)\"')
            session=requests.session()
            session.headers=headers_base
            response=session.get(url,verify=False)
            content=response.content
            xsrf=re.search(pattern,content)
            login_data['_xsrf']=xsrf.group(1).encode('utf-8')
            print xsrf.group(1)
            capcha_url='https://www.zhihu.com/captcha.gif?r=%d&type=login'%(time.time()*1000)
            print capcha_url
            capcha=session.get(capcha_url,stream=True,verify=False)
            f=open('capcha.gif','wb')
            f.write(capcha.content)
            f.close()
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
            rep=session.post(url_login,data=login_data,verify=False)
            print rep.status_code
            print rep.content
            mcookies=rep.cookies
            session.cookies=mcookies
            self.session=session
    def get_session(self):
        return self.session
def work():
    get_session=GetSession()
    session=get_session.get_session()
    r=session.get('https://www.zhihu.com/',verify=False)
    print r.content

if __name__=='__main__':
    work()
