#!/usr/bin/python
import re
input_points=[]
print u'please input validate code'
capcha_str=raw_input()
input_list=re.split(r' ',capcha_str)
for input_str in input_list:
		input_points.append(re.split(r','),input_str)
print input_points
