# task_master.py
# 1.生成任务，存入task队列
# 4.从网络result队列读取计算结果
# -*- coding:utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager


# 发送/接收任务的队列  -- 初始化。通过网络访问。
task_queue = queue.Queue()
result_queue = queue.Queue()

# 创建类（管理Queue）
class QueueManager(BaseManager):
    pass

# windows无法picklelambda函数，需自定义函数    
# 自定义函数 re_task_queue
def re_task_queue():
    global task_queue
    return task_queue

# 自定义函数 re_result_queue
def re_result_queue():
    global result_queue
    return result_queue

if __name__ == '__main__':    
    # 将两个队列注册到网络(封装)
    QueueManager.register('get_task_queue', callable = re_task_queue)
    QueueManager.register('get_result_queue', callable = re_result_queue)

    # 绑定端口5000，设置验证码
    manager = QueueManager(address = ('127.0.0.1', 5000), authkey = b'abc')

    # 启动Queue
    manager.start()

    # 获取通过网络访问的Queue对象(封装后操作)
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    # 读取任务
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout = 10)
        print('Result: %s' % r)
    
    # 关闭
    manager.shutdown()
    print('master exit.')
    
    
'''
E:\学海无涯\pythonLearning>python task_master.py
Put task 4568...
Put task 9046...
Put task 8976...
Put task 8442...
Put task 255...
Put task 8806...
Put task 8716...
Put task 258...
Put task 3972...
Put task 1049...
Try get results...
Result: 4568 * 4568 = 20866624
Result: 9046 * 9046 = 81830116
Result: 8976 * 8976 = 80568576
Result: 8442 * 8442 = 71267364
Result: 255 * 255 = 65025
Result: 8806 * 8806 = 77545636
Result: 8716 * 8716 = 75968656
Result: 258 * 258 = 66564
Result: 3972 * 3972 = 15776784
Result: 1049 * 1049 = 1100401
master exit.
'''