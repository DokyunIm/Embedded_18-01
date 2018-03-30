import sys
import smtplib
import codecs
import json
from email.mime.text import MIMEText

def send(From_Addr, To_Addr):
  key_file = open('./key.secret', 'r')
  key = json.loads(key_file.read())

  msg = MIMEText('Hello World')
  msg['Subject'] = 'Email example'
  msg['From'] = From_Addr
  msg['To'] = To_Addr

  smtp_gmail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  smtp_gmail.login(msg['From'], key['auth_key'])
  smtp_gmail.sendmail(msg['From'], msg['To'], msg.as_string())
  smtp_gmail.quit()
  return True

result = send('imjoshua9316dev@gmail.com', 'imjoshua9316@gmail.com')