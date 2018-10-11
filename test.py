# -*- coding:utf-8 -*-
#!/usr/bin/env python       # mac下使用PIL报错解决

from collections import Iterable
from functools import reduce
import re, os, time
import json
from multiprocessing import Process, Pool
import random
import subprocess
from multiprocessing import Process, Queue
import threading
from datetime import datetime, timedelta, timezone
from collections import namedtuple, deque
from collections import defaultdict, OrderedDict
from collections import Counter
import base64, struct
import hashlib, random, hmac
import itertools
from urllib import request,parse
import urllib
from xml.parsers.expat import ParserCreate

import ssl
# 针对mac处理 解决xml导入报错问题
ssl._create_default_https_context = ssl._create_unverified_context

from html.parser import HTMLParser
from html.entities import name2codepoint
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import requests
import chardet
from tkinter import *
import tkinter.messagebox as messagebox
import socket
from email.mime.text import MIMEText    # 负责构造邮件
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib      # 负责发送邮件
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr


# 格式化邮件地址 name <addr@example.com>
# Header编码处理中文
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


## 通过SMTP发出去
# 输入Email地址和口令
from_addr = 'chenweiqingme@126.com' # input('From: ')
password = 'chenwq004' # input('Password: ')
# 输入收件人地址
to_addr = '438024599@qq.com' # input('To: ')
# 输入SMTP服务器地址
smtp_server = 'smtp.126.com' # input('SMTP server: ')


## 电子邮件 SMTP协议
# 发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人


## 1/MUA把邮件发送到MTA
# 带附件的邮件
# 创建邮件对象
msg = MIMEMultipart('alternative')  #可以组合html和plain

msg['from'] = _format_addr('Python爱好者 <%s>' % from_addr)
# 接收字符串，而不是list。多个地址用,分隔
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候......', 'utf-8').encode()

# 邮件正文是MIMEText
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))



# 添加附件就是加上一个MIMEBase，从本地读取一个图片
with open(r'C:\Users\洛七\DeskTop\wedding.jpg', 'rb') as f:
    # 设置附件的MIME和文件名
    mime = MIMEBase('image', 'jpg', filename = 'wedding.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename = 'wedding.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-ID', '0')
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)
    

# print(msg)    


# 先把图片作为附件添加进去，再在html中引用。多个图片可以依次引用
msg.attach(MIMEText('<html><body><h1>Hello</h1><p><img src = "cid:0"></p></body></html>', 'html', 'utf-8'))




'''
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: base64
from: =?utf-8?b?UHl0aG9u54ix5aW96ICF?= <chenweiqingme@126.com>
To: =?utf-8?b?566h55CG5ZGY?= <438024599@qq.com>
Subject: =?utf-8?b?5p2l6IeqU01UUOeahOmXruWAmS4uLi4uLg==?=

aGVsbG8sIHNlbmQgYnkgUHl0aG9uLi4u
'''

#新建一个协议服务
server = smtplib.SMTP(smtp_server, 25)      #SMTP协议默认端口是25
# 打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
# 登陆邮箱
server.login(from_addr, password)
# 发送邮件，[to_addr]一次可以发送多人，list展示；as_sting把对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()



# 2/MUA从MTA收取邮件

