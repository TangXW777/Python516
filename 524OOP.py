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
## �����ǲ����Է���__name�� ����python���������__xxx�ı�������Ϊ_Student__name
#print(bart._Student__name)


# ================= �̳� ==================
class Animal(object):
	def run(self):
		print('animal is running...');

class Dog(Animal):
	def __len__(self):  # ��дlen()����
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
print(dir(dog));  # ��ȡ������������Է���

print(len('abc'));  # �ȼ�
print('abc'.__len__());

# �����һЩ���� 
# getattr()��setattr()�Լ�hasattr()


# ������
class Test(object):
	name = 'tang';
	
t = Test();
print(t.name);
print(Test.name);