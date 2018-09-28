import socket

## UDP协议
# TCP建立可靠连接，双方通信以流的形式发送数据
# UDP不需要建立连接，知道服务端地址和端口即可。传输速度快，但不一定能可靠到达

## 服务端
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))

# 不需要调用listen()方法，直接接收来自任何客户端的数据
print('Bind UDP on 9999...')
while True:
    #接收数据
    data, addr = s.recvfrom(1024)       #返回数据和客户端的地址与端口
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)    #UDP将数据发送给客户端
# 因为不是一对一的连接，所以需要发送地址
    