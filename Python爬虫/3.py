#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

##========  use requests & beautifulsoup4 ===============
import requests
from bs4 import BeautifulSoup
response = requests.get('http://jecvay.com');
soup = BeautifulSoup(response.text);

print(soup.title.text);
print(soup.body.text);

## 获取知乎登录页面的_xsrf 值
soup = BeautifulSoup(requests.get("https://www.zhihu.com/#signin").text);
print(soup.find("input", {"name": "_xsrf"})['value']);