#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

##===========  �����ļ���Ŀ¼ ================
#import os;
#print(os.name);  ##�����posix��˵��ϵͳ��Linux��Unix��Mac OS X�������nt������Windowsϵͳ
#os.uname(); ##��ϸ��Ϣ,������windows�ϲ��ṩ

#print(os.environ)  ##��������
#print(os.environ.get('JAVA_HOME'));
#
#print(os.path.abspath('.'));  ## ����·��

## ��ĳ��Ŀ¼�´���һ����Ŀ¼�����Ȱ���Ŀ¼������·����ʾ����:
#os.path.join('E:\Python516', 'testdir')
## Ȼ�󴴽�һ��Ŀ¼:
#os.mkdir('E:\Python516/testdir')
## ɾ��һ��Ŀ¼:
#os.rmdir('E:\Python516/testdir')

##============= ���л� ======================
import pickle
#d = dict(name='Bob', age=20, score=88);
#f = pickle.dumps(d);
#print(f);

## ����ֱ��д���ļ�
#d = dict(name='Bob', age=20, score=88);
#f = open('dump.txt', 'wb');
#pickle.dump(d, f);
#f.close();

## ��ȡ
#f = open('dump.txt', 'rb');
#d = pickle.load(f);
#f.close();
#print(d);

## =========== json��ʽ�� ===========
import json
#d = dict(name='Bob', age=20, score=88);
#f = json.dumps(d);
#print(f);

#json_str = '{"age":20, "score":88, "name":"Bob"}';
#f = json.loads(json_str);
#print(f);

## ============= ��һ��python classת��Ϊjson ================
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

##============ jsonת��Ϊpython class ===============
class Student(object):
	def __init__(self, name, age, score):
		self.name = name;
		self.age = age;
		self.score = score;
		
def dict2student(d):
	return Student(d['name'], d['age'], d['score']);
	
json_str = '{"age":20, "score":88, "name":"Bob"}';
print(json.loads(json_str, object_hook=dict2student)); 