#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP。绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据
s.bind(('127.0.0.1', 9995));
print('Bind UDP on 9996....');
while True:
	# 接收数据
	data, addr = s.recvfrom(1024);
	print('Received from %s:%s.' %addr);
	s.sendto(b'Hello, %s' %data, addr);
	
## 客户端程序在65_udp_2.py中