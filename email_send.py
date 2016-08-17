#!/usr/bin/python
#coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send(content):
	#receive='forniafu@163.com'
	receive='663693083@qq.com'
	#sender='forniafu@163.com'
	sender='663693083@qq.com'
	
	#message=MIMEText('hello , this is the first email i have sended to you ,please reply when you receive my email!','plain','utf-8')
	message=MIMEText(content,'html','utf-8')
	message['from']=sender
	message['to']=receive
	
	subject=u'今天抓到的租房信息'
	message['Subject']=Header(subject,'utf-8')
	
	print message;
	s=smtplib.SMTP_SSL()
	#s.connect('smtp.163.com',25)
	s.connect('smtp.qq.com',465)
	#s.login('forniafu@163.com','********')
	s.login('663693083@qq.com','********')
	s.sendmail(sender,receive,message.as_string())
	s.close()

if __name__=='__main__':
	send('内容')
