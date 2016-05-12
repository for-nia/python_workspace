#!/usr/bin/python
import urllib2
response=urllib2.urlopen("http://www.baidu.com")
print response.getcode()
print '------------'
print response.geturl()
print '------------'
print response.info()
#print response.read()
