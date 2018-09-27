import socket
import threading
from tcplink import tcplink

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


