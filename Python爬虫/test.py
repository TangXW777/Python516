#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

#import urllib
#import urllib.request
#
#url = 'http://www.baidu.com/'
#req = urllib.request.Request(url, headers = {
#    'Connection': 'Keep-Alive',
#    'Accept': 'text/html, application/xhtml+xml, */*',
#    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
#    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
#})
#oper = urllib.request.urlopen(req)
#data = oper.read()
#print(data)

import urllib.request
import requests
import http.cookiejar
from bs4 import BeautifulSoup
def makeMyOpener(head = {
	'Connection': 'Keep-Alive',
  'Accept': 'text/html, application/xhtml+xml, */*',
  'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
	cj = http.cookiejar.CookieJar();
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj));
	header = [];
	for key,value in head.items():
		elem = (key, value);
		header.append(elem);
	opener.addheaders = header;
	return opener;
	
def saveFile(dat):
	with open('temp.out', 'w') as f:
		soup = BeautifulSoup(dat);
		i = 1;
		for imgs in soup.find_all('img'):
			f.write(imgs.get('src')+'\n');

			print ('正在下载第'+str(i+1)+'张图片，图片地址为:http://www.ahpumec.edu.cn/' + imgs.get('src'))
			path = 'http://www.ahpumec.edu.cn/' + imgs.get('src');
			try:
				pic = requests.get(path, timeout=10);
			except requests.exceptions.ConnectionError:
				print('[错误]当前图片无法下载');
			string = 'pictures\\'+str(i)+'.jpg';
			fp = open(string.encode('cp936'), 'wb')
			fp.write(pic.content);
			fp.close();
			i = i + 1;

				

	
oper = makeMyOpener();
uop = oper.open('http://www.ahpumec.edu.cn/', timeout = 1000);
data = uop.read();
saveFile(data);