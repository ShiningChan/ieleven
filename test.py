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
from tkinter import *


# 从Frame派生出一个Application类，作为所有Widget的父容器
class Application(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.helloLabel = Label(self, text = 'Hello, world!')
        self.helloLabel.pack()  #把Widget加入到父容器中，并实现布局
        # command触发命令
        self.quitButton = Button(self, text = 'Quit', command = self.quit)
        self.quitButton.pack()
        

# 实例化Application，启动消息循环
app = Application()
#设置窗口标题
app.master.title('Hello World')
#主消息循环
app.mainloop()
    

    
    


