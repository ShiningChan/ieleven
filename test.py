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


# 创建一个socket（<Address Family>, <Type>）
# AF_INET指定使用IPv4协议，AF_INET6为IPv6（Internet进程间通信）
# AF_UNIX（同一台机器进程间通信）
# SOCK_STREAM指定使用面向流的TCP协议
# SOCK_DGRAM面向数据报的UDP协议

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接   参数是一个tuple，(<地址>, <端口号>)
# 域名自动转换到ip地址，Web服务的标准端口为80，SMTP服务标准端口是25
# <1024的是Internet标准服务端口，>1024的可以任意使用
s.connect(('www.sina.com.cn', 80))


# 发送数据
# 发送的文本格式必须符合HTTP标准。HTTP协议规定，客户端先发请求给服务端
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    # 每次最多接收1k字节 ---recv(max)方法
    d = s.recv(1024)
    if d:
        buffer.append(d)    # 多个1024位字符串为元素的list
    else:
        break

data = b''.join(buffer)     # 组合成一个长长长字符串

# 关闭连接
s.close()


## 接收到的数据包括HTTP头和网页本身
## 需要将HTTP头和网页分离，把HTTP头打印出来，网页内容保存到文件

print(data)

header, html = data.split(b'\r\n\r\n', 1)

print(header.decode('utf-8'))
# 把接收的数据写进文件
with open('sina.html', 'wb') as f:
    f.write(html)


