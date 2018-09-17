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

