import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender='1185946887@qq.com'
my_pass = 'svpmgkriyjhsidgd'
my_user='1185946887@qq.com'


def mail():
	msg = MIMEText('helloworld','plain','gbk')
	msg['From'] = formataddr(["FromRunoob", my_sender])
	msg['To'] = formataddr(["FK",my_user])
	msg['Subject'] = "hello"

	server=smtplib.SMTP_SSL("smtp.qq.com", 465)
	server.login(my_sender, my_pass)
	server.sendmail(my_sender,[my_user,],msg.as_string())
	server.quit()

mail()