# encoding:utf-8
import urllib
import urllib2
import os
import sys
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# USER_NAME = 'hyperionserver@163.com'
USER_NAME = 'luojiafei1234567@163.com'
PASSWD = 'paic1234'
SERNDER = USER_NAME


def send_email(body_text, title, receiver_list=['1196722167@qq.com']):
    msg = MIMEText(body_text, 'html', 'utf-8')
    msg['Subject'] = Header(title, 'utf-8')
    msg['To'] = ",".join(receiver_list)

    smtp = smtplib.SMTP()

    smtp.connect('smtp.163.com')
    # print smtp.ehlo()
    smtp.set_debuglevel(1)

    # # smtp.ehlo_or_helo_if_needed()
    # print smtp.starttls()

    smtp.login(USER_NAME, PASSWD)
    smtp.sendmail(SERNDER, receiver_list, msg.as_string())
    smtp.quit()


def main(body_text):
    if body_text != '':
        send_email(body_text, 'zealer test')


if __name__ == '__main__':
    main()
