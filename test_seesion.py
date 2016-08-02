#!/usr/bin/python

import get_session
import requests

session=get_session.getSession()
r=session.get('https://www.zhihu.com/')
print r.content
