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

# 解析XML时，注意找出自己感兴趣的节点，
# 响应事件时，把节点数据保存起来。
# 解析完毕后，就可以处理数据。

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

# 读取url对应网页数据
with request.urlopen(URL, timeout=4) as f:
    data = f.read()     #bytes型记得decode
    
    
'''
#定义解析类     
class WeatherSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
        
        
    def end_element(self, name):
        print('sax:end_element: %s' % name)
        
    def data_element(self, text):
        print('sax:char_data: %s' % text)
'''    

#定义解析类     
class WeatherSaxHandler(object):
    def start_element(self, name, attrs):
        global weather_dict, which_day
        # 判断并获取XML文档中地理位置信息
        # sax:start_element: yweather:location, attrs: {'xmlns:yweather': 'http://xml.weather.yahoo.com/ns/rss/1.0', 'city': 'Beijing', 'country': 'China', 'region': ' Beijing'}
        # sax:end_element: yweather:location
        if name == 'yweather:forecast':
            weather_dict['city'] = attrs['city']
        
    def end_element(self, name):
        print('sax:end_element: %s' % name)
        
    def data_element(self, text):
        print('sax:char_data: %s' % text)
        
        
handler = WeatherSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.data_element

## parser.Parse(data.decode('utf-8'))

weather_dict = {}
which_day = 0



'''
def parseXml(xml_str):
    print(xml_str)
    return{
        'city': '?'
        'forecast':[
            {
                'date': '2017-11-17',
                'high': 43,
                'low' : 26
            },
            {
                'date': '2017-11-18',
                'high': 41,
                'low': 20
            },
            {
                'date': '2017-11-19',
                'high': 43,
                'low': 19
            }
        ]
    }
    '''