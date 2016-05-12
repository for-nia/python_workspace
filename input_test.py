#!/usr/bin/python
import re
print 'please input tow param'
input=raw_input()
a=[]
p=re.compile(r' ')
input_list=re.split(p,input)
print input
for str in input_list:
	a.append(re.split(r',',str))
print a


