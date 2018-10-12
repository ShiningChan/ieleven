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
import poplib       #负责下载邮件
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.parser import Parser
from email.header import decode_header


# 2/MUA从MTA收取邮件
# 编写一个MUA作为客户端，从MDA把邮件获取到电脑或者手机上
#step1 用poplib把邮件的原始文本下载到本地
#step2 用email解析原始文本，还原为邮件对象

# 输入邮件地址、口令和pop3服务器地址
email = '438024599@qq.com'  #input('Email: ')
password = 'ztxxqglnshdscbdh' #input('password: ')
pop3_server = 'pop.qq.com' # input(POP3 server: )

# 连接到pop3服务器
server = poplib.POP3(pop3_server)
# 可以打开或关闭调试信息
server.set_debuglevel(1)
# 可选：打印pop3服务器的欢迎文字
print(server.getwelcome().decode('utf-8'))


# 身份认证
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间
print('Message: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184']
print(mails)

# 获取最新一封邮件。注意索引号从1开始
index = len(mails)
resp, lines, octets = server.retr(index)    #循环使用可将每一封邮件内容都拿到

# lines存储了邮件的原始文本的每一行
# 可以获得整个邮件的原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')
#稍后解析出邮件：
msg = Parser().parsestr(msg_content)


# 可以根据邮件索引号直接从服务器删除邮件
# server.dele(index)
# 关闭连接
server.quit()

print('-------------------以下为邮件原始文本-----------')
print(msg)
print('-------------------以上为邮件原始文本-----------')
## Message对象本身可能是一个MIMEMultipart对象，包含嵌套的其他MIMEBase对象
# 可能多层嵌套。因此要递归打印出Message对象的层次结构

'''
#indent用于缩进显示
def print_info(msg, indent = 0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject'
                    value = decode_str(value)
                else:
                    '''