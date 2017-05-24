#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a = sorted([2,3,-5,-34], key=abs);
#print(a);

# ====== 返回函数 ===========
#def sum(*args):
#	ax = 0;
#	for n in args:
#		 ax = ax + n;
#	return ax;
#a = sum(*[2,3,-5,-34]);
#print(a);

# 返回求和函数
#def lazy_sum(*args):
#	def sum():
#		ax = 0;
#		for n in args:
#			ax = ax + n;
#		return ax;
#	return sum;
#
#f = lazy_sum(*[2,3,-5,-34]);
#f2 = lazy_sum(*[2,3,-5,-33]);
#print(f);
#print(f2);
#print(f());
#print(f2());



# ====== 匿名函数 ===========
#def f(x, y):
#	return lambda: x * x + y * y;
#
#print(f(2, 3)());


# ====== 装饰器 ===========
def log(func):
	def wrapper(*args, **kw):
		print('call %s()' % func.__name__);
		return func(*args, **kw);
	return wrapper;

@log
def now():
	print('2017-5-24');

now();
print(now.__name__);# wrapper

####
import functools
def log2(text):
	def decorator(func):
		@functools.wraps(func) # 可以不改变__name__
		def wrapper(*args, **kw):
			print('%s %s' % (text, func.__name__));
			return func(*args, **kw);
		return wrapper;
	return decorator;
	
@log2('execute')
def now2():
	print('2017-5-24');
	
now2();
print(now2.__name__);