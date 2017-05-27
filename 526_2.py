#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

##======== 定制类 ==========

##======== __str__ ==========
#class Student(object):
#	def __init__(self, name):
#		self.name = name;
#	def __str__(self):  ## 类似java的toString()
#		return 'Student object (name: %s)' % self.name;
#	__repr__ = __str__;  ## __repr__是给程序开发者看的，通常两个一样
#print(Student('tang'));
#a = Student('tang');
#print(a.__repr__());


## ============ __iter__ ================
#class Fib(object):
#	def __init__(self):
#		self.a, self.b = 0, 1; ## 初始化两个计算器
#		
#	def __iter__(self):S
#		return self;  ## 实力本身就是迭代对象，故返回自己
#		
#	def __next__(self):
#		self.a, self.b = self.b, self.a + self.b; ## 计算下一个值
#		if self.a > 10000:
#			raise StopIteration(); ## 退出循环
#		return self.a; ## 返回下一个值
#
#for n in Fib():
#	print(n);

## 取出某一个值 __getitem__
#def __getitem__(self, n):
#	a, b = 1, 1
#	for x in range(n):
#		a, b = b, a + b;
#	return a;
#	
#from types import MethodType  ## 动态添加方法
#Fib.__getitem__ = __getitem__;
#
#f = Fib();
#print(f[0]);
#print(f[5]);

## 类似list的切片功能
#def __getitem__(self, n):
#	if isinstance(n, int):
#		a, b = 1, 1;
#		for x in range(n):
#			a, b = b, a + b;
#		return a;
#	if isinstance(n, slice):  ## 如果是切片
#		start = n.start;
#		stop = n.stop;
#		if start is None:
#			start = 0;
#		a, b = 1, 1;
#		L = [];
#		for x in range(stop):
#			if x >= start:
#				L.append(a);
#			a, b = b, a + b;
#		return L;
#
#from types import MethodType  ## 动态添加方法
#Fib.__getitem__ = __getitem__;
#		
#f = Fib();
#print(f[4:7]);
#print(f[:10]);
#print(f[3]);

## 动态添加属性
#class Student(object):
#	def __getattr__(self, attr):
#		if attr == 'age':
#			return lambda: 25;  ## 返回一个函数
#		elif attr == 'score':
#			return 99;  ## 直接返回值
#
#s = Student();
#print(s.age());
#print(s.score);
#print(s.name);  ## None，因为__getattr__默认返回None


##============= 链式调用 ==================
#class Chain(object):
#	def __init__(self, path=''):
#		self._path = path;
#		
#	def __getattr__(self, path):
#		return Chain('%s/%s' %(self._path, path));
#
#	def __str__(self):
#		return self._path;
#		
#	__repr__ = __str__;
#
#print(Chain().status.user.timeline.list);

##============= 实例本身调用方法 ==================
class Student(object):
	def __init__(self, name):
		self.name = name;
	
	def __call__(self):
		print('My name is %s' % self.name);
		
s = Student('tang');
s();   ## 实例直接调用方法

print(callable(Student('tang')));  ## True 判断是否是“可调用”对象
