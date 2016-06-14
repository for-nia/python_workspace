#!/usr/bin/python

import get_session
import requests

Getsession=get_session.GetSession()
session=GetSession.get_session()
r=session.get('https://www.zhihu.com/people/junlin_1980')
junlin=open('junlin.html',wb)
junlin.write(r)
junlin.close()
print r.content
