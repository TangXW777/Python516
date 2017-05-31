#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

##============ io ==============
#def ioTest():
#	f = open('test.txt');
#	content = f.read();
#	print(content);
#	f.close();
	
##======== 使用with自动关闭 ===============
#def ioTest():
#	with open('test.txt','r') as f:
#		print(f.read());
#
#ioTest()
## 如果要读取图片视频，可以通过rb模式打开
## 指定编码打开
## f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
## 遇到一些编码不规范的
##  f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')	




## 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
#def ioTest():
#	with open('test.txt','w') as f:
#		f.write('hello world!');
#		
#ioTest();

##很多时候，数据读写不一定是文件，也可以在内存中读写。
##StringIO顾名思义就是在内存中读写str。
##要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可

from io import StringIO

def test1():
	f = StringIO();
	f.write('hello');
	print(f.getvalue());
test1();

def test2():
	f = StringIO('Hello!\nHi!\nGoodbye');
	while True:
		s = f.readline();
		if s == '':
			break;
		print(s.strip());
		
test2();


##StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
##BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes

from io import BytesIO
f = BytesIO();
f.write('中文'.encode('UTF-8'));
print(f.getvalue());