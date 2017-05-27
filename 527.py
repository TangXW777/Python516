#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

##================ 枚举 ================
#from enum import Enum, unique
#
#Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'));
#print(Month.Jan);
#for name, member in Month.__members__.items():
#	print(name, '=>', member, ',', member.value);
	
## value属性则是自动赋给成员的int常量，默认从1开始计数
## 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类

#@unique
#class Weekday(Enum):
#	Sun = 0 # Sun的value被锁定为0
#	Mon = 1
#	Tue = 2
#	Web = 3
#	Thu = 4
#	Fri = 5
#	Sat = 6
	
## @unique装饰器可以帮助我们检查保证没有重复值
#print(Weekday.Mon)
#
#for name, member in Weekday.__members__.items():
#	print(name, '=>', member, ', value = >', member.value);

##=============== 使用元类 =======================
#from hello import Hello
#h = Hello();
#h.hello();
#print(type(Hello));
#print(type(h));

## =========== 通过type()函数动态创建Hello =============
def fn(self, name='world'):
	print('Hello, %s' %name);

## 动态创建Hello class
Hello = type('Hello', (object,), dict(hello=fn));
h = Hello();
h.hello();