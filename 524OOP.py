#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
#==========  OOP =================
# 1.public property
#class Student(object):
#	def __init__(self, name, score):
#		self.name = name;
#		self.score = score;
#		
#	def print_score(self):
#		print('%s: %s' % (self.name, self.score));
#
#
#bart = Student('Bart Simpson', 59);
#lisa = Student('Lisa Simpson', 87);
#bart.print_score();
#lisa.print_score();


# 2. private property
#class Student(object):
#	def __init__(self, name, score):
#		self.__name = name;
#		self.__score = score;
#		
#	def print_score(self):
#		print('%s: %s' % (self.__name, self.__score));
#
#
#bart = Student('Bart Simpson', 59);
#lisa = Student('Lisa Simpson', 87);
#bart.print_score();
#lisa.print_score();
#print(bart.__name);
## 并不是不可以访问__name， 而是python解释器会把__xxx的变量，变为_Student__name
#print(bart._Student__name)


# ================= 继承 ==================
class Animal(object):
	def run(self):
		print('animal is running...');

class Dog(Animal):
	def __len__(self):  # 覆写len()方法
		return 6; 
	pass
class Cat(Animal):
	pass
	
dog = Dog();
dog.run();
print(len(dog));
cat = Cat();
cat.run();
print(isinstance(dog, Animal));
print(dir(dog));  # 获取对象的所有属性方法

print(len('abc'));  # 等价
print('abc'.__len__());

# 对象的一些方法 
# getattr()、setattr()以及hasattr()


# 类属性
class Test(object):
	name = 'tang';
	
t = Test();
print(t.name);
print(Test.name);