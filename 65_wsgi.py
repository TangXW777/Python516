#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

from wsgiref.simple_server import make_server
from wsgihello import application

httpd = make_server('', 8000, application);
print('Serving HTTP on port 8000...');
## 开始监听Http请求
httpd.serve_forever();