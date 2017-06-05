#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

## Object-Relational Mapping，把关系数据库的表结构映射到对象上
## 导入SQLAlchemy，并初始化DBSession
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

## 创建对象的基类
Base = declarative_base();
class Test(Base):
	# 表的名字
	__tablename__ = 'test';
	
	# 表的结构
	id = Column(String(20), primary_key=True);
	name = Column(String(50));
	
## 初始化数据库连接
engine = create_engine('mysql+pymysql://root:root@localhost:3306/ehow');
## 创建DBSession类型
DBSession = sessionmaker(bind=engine);

## 创建session对象
session = DBSession();
new_user = Test(id='2', name='Bob');
session.add(new_user);
session.commit();
session.close;

## 查询操作等另添