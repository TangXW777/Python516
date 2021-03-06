#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

## 导入socket库
import socket, threading, time

## 创建一个socket
## AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
#
### 建立连接
#s.connect(('www.sina.com.cn', 80));
#
### 发送数据
#s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
### 接收数据
#buffer = [];
#while True:
#	# 每次堆垛接收1k字节
#	d = s.recv(1024);
#	if d:
#		buffer.append(d);
#	else:
#		break;
#
#data = b''.join(buffer);
#
#s.close()
#
#header, html = data.split(b'\r\n\r\n', 1);
#print(header.decode('utf-8'));
## 把接收的数据写入文件
#with open('sina.html', 'wb') as f:
#	f.write(html);

##========== 以下模仿client/server对话 ===============
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
# 监听端口
s.bind(('127.0.0.1', 9997))
s.listen(5); # 最大连接数
print('Waiting for connection...');

def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % addr);
	sock.send(b'Welcome!');
	while True:
		data = sock.recv(1024);
		time.sleep(1);
		if not data or data.decode('utf-8') == 'exit':
			break;
		sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'));
	sock.close();
	print('Connection from %s:%s closed.' % addr);

while True:
	# 接受一个新连接
	sock, addr = s.accept();
	# 创建新线程来处理TCP连接
	t = threading.Thread(target=tcplink, args=(sock, addr));
	t.start();
	



## 客户端程序在61_tcp_2.py中
