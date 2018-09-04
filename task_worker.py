# task_worker.py
# -*- coding:utf-8 -*-

import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager
class QueueManager(BaseManager):
    pass
    

# 这个QM只从网络上获取Queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器（运行task_master.py的机器）
server_addr = '127.0.0.1'
print('Connet to server %s...' % server_addr)
# 端口和验证码
m = QueueManager(address = (server_addr, 5000), authkey = b'abc')

# 从网络连接
m.connect()

# 获取Queue的对象
# 2.从网络task队列中读取任务
# 3.计算任务结果，并从网络存入result队列

task = m.get_task_queue()
result = m.get_result_queue()

# 从task队列获取任务，并写入result队列
for i in range(10):
    try:
        n = task.get(timeout = 1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
        
# 处理结束
print('worker exit.')        

'''
E:\学海无涯\pythonLearning>python task_worker.py
Connet to server 127.0.0.1...
run task 4568 * 4568...
run task 9046 * 9046...
run task 8976 * 8976...
run task 8442 * 8442...
run task 255 * 255...
run task 8806 * 8806...
run task 8716 * 8716...
run task 258 * 258...
run task 3972 * 3972...
run task 1049 * 1049...
worker exit.
'''