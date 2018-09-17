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
# import ssl
# 针对mac处理 解决xml导入报错问题
# ssl._create_default_https_context = ssl._create_unverified_context
from html.parser import HTMLParser
from html.entities import name2codepoint
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import requests
import chardet



## 获取CPU信息
# CPU逻辑数量
psutil.cpu_count()
4
# CPU物理核心
psutil.cpu_count(logical = False)
2       # 双核超线程， 4则是4核非超线程


# 统计CPU的用户、系统、空闲时间
psutil.cpu_times()
scputimes(user=8915.4375, system=7503.78125, idle=195506.48437499997, interrupt=173.640625, dpc=148.6875)


for x in range(10):
    psutil.cpu_percent(interval = 1, percpu = True)

'''
[9.2, 4.7, 6.2, 3.1]
[4.7, 3.1, 6.2, 9.4]
[24.6, 29.7, 35.9, 25.0]
[3.1, 0.0, 1.6, 12.5]
[4.7, 6.2, 1.6, 7.8]
[1.6, 0.0, 4.7, 7.8]
[6.2, 3.1, 3.1, 7.8]
[24.6, 31.2, 21.9, 21.9]
[16.7, 4.7, 14.1, 12.5]
[10.8, 1.6, 3.1, 3.1]
'''


## 获取内存信息
# 获取物理内存
psutil.virtual_memory()
# svmem(total=8589934592, available=2866520064, percent=66.6, used=7201386496, free=216178688, active=3342192640, inactive=2650341376, wired=1208852480)
# （字节）总内存 8GB，已使用6.7GB，使用率66.6%

# 交换区内存信息
psutil.swap_memory()
#sswap(total=1073741824, used=150732800, free=923009024, percent=14.0, sin=10705981440, sout=40353792)


## 获取磁盘信息
psutil.disk_partitions() # 磁盘分区信息
[sdiskpart(device='/dev/disk1', mountpoint='/', fstype='hfs', opts='rw,local,rootfs,dovolfs,journaled,multilabel')]
# HFS 文件格式  rw 可读写 journaled 支持日志

psutil.disk_usage('/') # 磁盘使用情况
sdiskusage(total=998982549504, used=390880133120, free=607840272384, percent=39.1)

psutil.disk_io_counters() # 磁盘IO
sdiskio(read_count=988513, write_count=274457, read_bytes=14856830464, write_bytes=17509420032, read_time=2228966, write_time=1618405)


## 获取网络接口和网络连接信息
psutil.net_io_counters() # 获取网络读写字节／包的个数
#snetio(bytes_sent=3885744870, bytes_recv=10357676702, packets_sent=10613069, packets_recv=10423357, errin=0, errout=0, dropin=0, dropout=0)

psutil.net_if_addrs() # 获取网络接口信息
{
  'lo0': [snic(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0'), ...],
  'en1': [snic(family=<AddressFamily.AF_INET: 2>, address='10.0.1.80', netmask='255.255.255.0'), ...],
  'en0': [...],
  'en2': [...],
  'bridge0': [...]
}

psutil.net_if_stats() # 获取网络接口状态
{
  'lo0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=16384),
  'en0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1500),
  'en1': snicstats(...),
  'en2': snicstats(...),
  'bridge0': snicstats(...)
}


$ sudo python3      # 获取系统权限

psutil.net_connections()    # 获取当前网络连接信息
[
    sconn(fd=83, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::127.0.0.1', port=62911), raddr=addr(ip='::127.0.0.1', port=3306), status='ESTABLISHED', pid=3725),
    sconn(fd=84, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::127.0.0.1', port=62905), raddr=addr(ip='::127.0.0.1', port=3306), status='ESTABLISHED', pid=3725),
    sconn(fd=93, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::', port=8080), raddr=(), status='LISTEN', pid=3725),
    sconn(fd=103, family=<AddressFamily.AF_INET6: 30>, type=1, laddr=addr(ip='::127.0.0.1', port=62918), raddr=addr(ip='::127.0.0.1', port=3306), status='ESTABLISHED', pid=3725),
    sconn(fd=105, family=<AddressFamily.AF_INET6: 30>, type=1, ..., pid=3725),
    sconn(fd=106, family=<AddressFamily.AF_INET6: 30>, type=1, ..., pid=3725),
    sconn(fd=107, family=<AddressFamily.AF_INET6: 30>, type=1, ..., pid=3725),
    ...
    sconn(fd=27, family=<AddressFamily.AF_INET: 2>, type=2, ..., pid=1)
]



## 寻找python所在进程
for i in list_pid:
    try:
        m = psutil.Process(i)
            if re.match('.ython*', m.name()) is not None:
                print(i)
    finally:
        print('Not found')

Not found
14276
Not found
Not found
Not found
