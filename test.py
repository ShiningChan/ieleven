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

## 服务端 ##

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定监听的地址和端口
# （服务器同时响应多个客户端请求，需要绑定一个端口并监听连接）

# 服务器可能有多块网卡，可以绑定到某一块网卡的ip上
# 0.0.0.0绑定到所有的网络地址
# 127.0.0.1绑定到本机地址，客户端必须在本机运行才能连接
# 端口号需预先指定。小于1024的端口号必须要管理员权限才能绑定

# 绑定端口
s.bind(('127.0.0.1', 9999))

# 监听
s.listen(5)     #指定等待连接的最大数量
print('Waiting for connection...')


while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接。传入函数、参数
    t = threading.Thread(target = tcplink, args = (sock, addr))
    t.start()

    
# 每个连接都必须创建新线程（或进程）来处理

def tcplink(sock, addr)：
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


## 客户端 ##
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据：
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()

