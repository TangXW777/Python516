#！usr/bin/env python3
# -*- encoding: utf-8 -*-

# ========== 返回函数 ==========
# 闭包
#def lazy_sum(*args):
#	def sum():
#		ax = 0;
#		for n in args:
#			ax = ax + n;
#		return ax;
#	return sum;
#	
#f = lazy_sum(1, 3, 5, 7, 9);
#print(f);
#print(f());

def count():
	fs = [];
	for i in range(1, 4):
		def f():
			return i * i;
		fs.append(f);
	return fs;
f1, f2, f3 = count();
print(f1());
# 9
print(f2());
# 9
print(f3());
# 9

#========= 匿名函数lambda =========
a = list(map(lambda x: x * x,[1, 2, 3, 4]));
print(a);

#============= 装饰器Decorator =========================
#def now():
#	print('it is now');
#f = now;
#f();
#print(now.__name__);

#def log(func):
#	def wrapper(*args, **kw):
#		print('call %s():' % func.__name__);
#		return func(*args, **kw);
#	return wrapper;

import functools
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s()' %(text, func.__name__));
			return func(*args, **kw);
		return wrapper;
	return decorator;
	
@log('execute')
def now():
	print('it is now');

now();

# 不带@functools.wraps(func)
print(now.__name__); # wrapper
# 带@functools.wraps(func) 为now

