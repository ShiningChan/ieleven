# -*- coding:utf-8 -*-


import unittest
from mydict import Dict
        
class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp...')
        
    def test_init(self):
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)    # 断言返回的结果与1相等
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
        
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
        
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
        
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):   # 期待抛出指定类型的Error
            value = d['empty']
            
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError): # 期待抛出指定类型的Error
            value = d.empty
            
    def tearDown(self):
        print('tearDown...\n')
       
## 可以自己执行
if __name__ == '__main__':
    unittest.main()

    
# 命令行执行
## $ python -m unittest mydict_test