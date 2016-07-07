import smtplib
from email.mime.text import MIMEText
from email.header import Header

receive='663693083@qq.com'
sender='forniafu@163.com'

message=MIMEText('this is a python main','plain','utf-8')
message['From']=sender
message['To']=receive

subject='first mail'
message['Subject']=subject

s=smtplib.SMTP()
s.connect('smtp.163.com',25)
s.login('forniafu@163.com','hello2world')
s.sendmail(sender,receive,message.as_string())
s.close()


