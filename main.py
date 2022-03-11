
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
email = "email@gmail.com"
pas = ""
sms_gateway = '##########0@txt.bell.ca'
#sms_gateway = '##########@mms.fido.ca'
#sms_gateway = '##########@vmobile.ca'
smtp = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(smtp,port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(email,pas)
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = sms_gateway
msg['Subject'] = "\n"
body = "message here\n"
msg.attach(MIMEText(body, 'plain'))
sms = msg.as_string()
#server.send_message(sms)
server.sendmail(email,sms_gateway,sms)
server.close()

