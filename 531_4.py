#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

##===========  操作文件和目录 ================
#import os;
#print(os.name);  ##如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
#os.uname(); ##详细信息,但是在windows上不提供

#print(os.environ)  ##环境变量
#print(os.environ.get('JAVA_HOME'));
#
#print(os.path.abspath('.'));  ## 绝对路径

## 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
#os.path.join('E:\Python516', 'testdir')
## 然后创建一个目录:
#os.mkdir('E:\Python516/testdir')
## 删掉一个目录:
#os.rmdir('E:\Python516/testdir')

##============= 序列化 ======================
import pickle
#d = dict(name='Bob', age=20, score=88);
#f = pickle.dumps(d);
#print(f);

## 或者直接写入文件
#d = dict(name='Bob', age=20, score=88);
#f = open('dump.txt', 'wb');
#pickle.dump(d, f);
#f.close();

## 读取
#f = open('dump.txt', 'rb');
#d = pickle.load(f);
#f.close();
#print(d);

## =========== json格式化 ===========
import json
#d = dict(name='Bob', age=20, score=88);
#f = json.dumps(d);
#print(f);

#json_str = '{"age":20, "score":88, "name":"Bob"}';
#f = json.loads(json_str);
#print(f);

## ============= 把一个python class转换为json ================
#class Student(object):
#	def __init__(self, name, age, score):
#		self.name = name;
#		self.age = age;
#		self.score = score;
#	
#s = Student('Bob', 20, 88);
# print(json.dumps(s));  ## typeerror
#def student2dict(std):
#	return {
#		'name' : std.name,
#		'age' : std.age,
#		'score' : std.score
#	}
#	
#print(json.dumps(s, default=student2dict));

##============ json转换为python class ===============
class Student(object):
	def __init__(self, name, age, score):
		self.name = name;
		self.age = age;
		self.score = score;
		
def dict2student(d):
	return Student(d['name'], d['age'], d['score']);
	
json_str = '{"age":20, "score":88, "name":"Bob"}';
print(json.loads(json_str, object_hook=dict2student)); 