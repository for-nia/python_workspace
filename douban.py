#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import email_send
data=[]
headers_base = {
		'Accept-Encoding':'gzip, deflate',
		'Accept-Language':'en,zh-CN;q=0.8,zh;q=0.6',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'site.douban.com',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
		'X-Requested-With':'XMLHttpRequest'
		}
def work(tag):
	url='https://site.douban.com/227778/widget/forum/15931820/?start='+str(tag*30)
	session=requests.session()
	response=session.get(url,headers=headers_base,verify=False)
	content=response.content
	#print content
	soup=BeautifulSoup(content)
	table=soup.find('table',attrs={'class':'list-b'})
	#print table
	rows=table.find_all('tr')
	for row in rows:
		cols = row.find_all('td')
		#cols = [ele.text.strip() for ele in cols]
		td=cols[0]
		a=td.find('a')
		if a is not None:
			print a['href']
			if(parse(session,a['href'])):
				data.append(a.prettify()+'<br/>')
		else:
			print 'not found'
		#print td
		#data.append([ele for ele in cols if ele])
	#print ''.join(data)
	#email_send.send(''.join(data))
def parse(session,url):
	response=session.get(url,headers=headers_base,verify=False)
	content=response.content
	soup=BeautifulSoup(content)
	p=soup.find('p',attrs={'id':'link-report'})
	if p is not None:
		#print str(p.contents).decode('unicode')
		p_con=p.prettify()
		#print p.prettify()
		patern=re.compile(u'桃园|西乡|坪洲')
		r=re.search(patern,p_con)
		if r:
			#print p_con
			return True
		else:
			return False
	#print p
if __name__=='__main__':
	for i in range(0,3):
		work(i)
	email_send.send(''.join(data))
