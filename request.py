#!/urs/bin/python

import requests

r=requests.get('http://www.baidu.com')
html=r.content
header=r.headers
print header
print html

