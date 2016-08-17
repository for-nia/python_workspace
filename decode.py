#!/usr/bin/python
#-*- coding utf-8 -*-
import sys 
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入 
sys.setdefaultencoding('utf-8'))
s=u'你好世界'
print s.decode('utf-8')
