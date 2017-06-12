#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

import urllib
import urllib.request
#url = 'http://www.baidu.com';
#data = urllib.request.urlopen(url).read();
#data = data.decode('UTF-8');
#print(data);

#data = {};
#data['word'] = 'Jecvay Notes';
#
#url_values = urllib.parse.urlencode(data);
#url = 'http://www.baidu.com/s?';
#full_url = url + url_values;
#print(full_url);
#
#data = urllib.request.urlopen(full_url).read();
#print(data);

## ======== collection.deque =========
#from collections import deque
#queue = deque(['Eric', 'John', 'Michael']);
#queue.append('Terry');
#print(queue.popleft());   ## 队首元素出队 Eric
#print(queue.popleft()); ## John
#print(queue);  ## deque(['Michael', 'Terry'])
#
#a = set('abracadabra');  ## 创建一个set
#b = set('alacazam');
#print(a - b);

import re
from collections import deque

queue = deque();
visited = set();

url = 'http://www.aiit.edu.cn';
queue.append(url);
cnt = 0;
while queue:
	url = queue.popleft();  ## 队首出队
	visited |= {url} ;
	print(visited);
	
	print('已经抓取:' + str(cnt) + '  正在抓取 <---' + url);
	cnt += 1;
	urlop = urllib.request.urlopen(url,timeout=100);
	print(urlop.getheader('Content-Type'))
	if 'html' not in urlop.getheader('Content-Type'):
		#print(urlop.getheader('Content-Type'))
		continue;
	## 避免程序异常终止
	try:
		data = urlop.read().decode('utf-8');
	except:
		continue;
		
	## 正则表达式提取页面中所有队列，并判断是否已经访问过，然后加入待爬队列
	linkre = re.compile('href="(.+?)"');
	for x in linkre.findall(data):
		if 'http' in x and x not in visited:
			queue.append(x);
			print('加入队列 --->' + x);
