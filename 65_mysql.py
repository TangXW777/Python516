#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

## 由于mysql的驱动只支持到python3.4，而这里是python3.5
## 所以用pymysql
import pymysql
conn = pymysql.connect(user='root', password='root',database='ehow',charset='UTF8');
cursor = conn.cursor();

## 运行查询
cursor.execute('select * from user');
values = cursor.fetchall();
print(values);