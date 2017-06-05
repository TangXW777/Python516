#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
from email.mime.text import MIMEText

## 构造简单的纯文本邮件
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8');

## 输入Email地址和口令
from_addr = input('From:');
password = input('Password:');
## 输入收件人地址
to_addr = input('To:');
## 输入SMTP服务器地址：
smtp_server = input('SMTP server:');

import smtplib
## SMTP协议默认端口是25
server = smtplib.SMTP(smtp_server, 25);
server.set_debuglevel(1);
server.login(from_addr, password);
server.sendmail(from_addr, [to_addr], msg.as_string());
server.quit();