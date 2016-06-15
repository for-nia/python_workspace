#!/usr/bin/python

import get_session
import requests

getsession=get_session.GetSession()
session=getsession.get_session()
r=session.get('https://www.zhihu.com/people/junlin_1980')
junlin=open('junlin.html','wb')
junlin.write(r.content)
junlin.close()
print r.content
