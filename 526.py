#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# ============ 动态给对象绑定属性和方法 ==================
#class Student(object):
#	pass
#
#s = Student();
#s.name = 'Michael';
#print(s.name);
#
#def set_age(self, age):
#	self.age = age;
#	
#from types import MethodType
#s.set_age = MethodType(set_age, s);
#s.set_age(25);
#print(s.age);  
## 这种方法只针对绑定的对象，要是所有实例都绑定方法，可以给class绑定方法
#def set_score(self, score):
#	self.score = score;
#
#Student.set_score = set_score;
#s.set_score(100);
#print(s.score);


## 使用__slots__
## 只允许对Student实例添加name和age属性
## 注意__slots__只对当前类实例起作用，子类无效
#class Student(object):
#	__slots__ = ('name', 'age');  # 用tuple定义允许绑定的属性名称
#	
#s = Student();
#s.name = 'tang';
#s.age = 25;
#s.score = 97;  # error


## 对对象的属性赋值做判断
#s = Student();
#s.score = 9999; ## 显然是错误的
#class Student(object):
#	def get_score(self):
#		return self.score;
#	def set_score(self, value):
#		if not isinstance(value, int):
#			raise ValueEoor('score must be an integer');
#		if value < 0 or value > 100:
#			raise ValueError('score must between 0 ~ 100!');
#		self.score = value;
#		
#s = Student();
#s.set_score(99);
#print(s.get_score());

## 但是上面的方法有问题，比如直接赋值属性还是可以赋值错误值
## 还有就是没有直接赋值那么简单
## @property装饰器就是负责把一个方法变成属性调用的
class Student(object):
	@property
	def score(self):
		return self._score;
		
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueEoor('score must be an integer');
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!');
		self._score = value;
		
s = Student();
#s.score = 999;  ## error
s.score = 99;
print(s.score);
## 如果之定义score的@property，没有定义@score.setter说明只是一个只读属性

		
