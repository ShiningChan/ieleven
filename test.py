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
from email.mime.text import MINEText    # 负责构造邮件
import smtplib      # 负责发送邮件

## 电子邮件 SMTP协议
# 发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

## 1/MUA把邮件发送到MTA
# 构造简单纯文本  
# <参数1> - 邮件正文， <参数2> - subtype(plain表示纯文本)，编码保证多语言兼容性
msg = MINEText('hello, send by Python...', 'plain', 'utf-8')

## 通过SMTP发出去
# 输入Email地址和口令
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址
to_addr = input('To: ')
# 输入SMTP服务器地址
smtp_server = input('SMTP server: ')

#新建一个协议
server = smtplib.SMTP(smtp_server, 25)      #SMTP协议默认端口是25
# 
server.set_debuglevel(1)
# 登陆邮箱
server.login(from_addr, password)
# 发送邮件 
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()



# 2/MUA从MTA收取邮件


