# -*- coding:utf-8 -*-

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
# 针对mac处理
# ssl._create_default_https_context = ssl._create_unverified_context
from html.parser import HTMLParser
from html.entities import name2codepoint
from PIL import Image, ImageFilter, ImageDraw, ImageFont

'''
## 图片大小缩放

# 打开一个jpg图像文件
im = Image.open('test.jpg')
# 获取图像尺寸
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%
im.thumbnail((w//2, h//2))      #取整除法
print('Resize image to: %sx%s' %(w//2, h//2))
# 把缩放后的图像用jpeg格式保存
im.save('thumbnail.jpg', 'jpeg')


## 图片模糊效果

im = Image.open('test.jpg')
# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

'''

## 绘图方法。生成字母验证码图片。

# 随机字母 返回数值表达式sting型
def rndChar():
    return chr(random.randint(65, 90))
    
# 随机颜色1
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
    
# 随机颜色2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
    

# 240 * 60 初始化画布
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Draw对象 画布内
draw = ImageDraw.Draw(image)

# 填充每个像素 画布
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill = rndColor())
        
# 创建Font对象
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)

# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font = font, fill = rndColor2())
    
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')