#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

##========= threadlocal ==========

##如果用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象如何？
#global _dict = {};
#def std_thread(name):
#	std = Student(name);
#	global_dict[threading.current_thread()] = std;
#	do_task_1();
#	do_task_2();
#	
#def do_task_1():
#	std = global_dict[threading.current_thread()];
#	
#def do_task_2():
#	std = global_dict[threading.current_thread()];
	
##这种方式理论上是可行的，它最大的优点是消除了std对象在每层函数中的传递问题，但是，每个函数获取std的代码有点丑。

## ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事：
import threading

# 创建全局threadlocal对象
local_school = threading.local();

def process_student():
	# 获取当前线程关联的student
	std = local_school.student;
	print('Hello, %s (in %s)' % (std, threading.current_thread().name));
	
def process_thread(name):
	# 绑定ThreadLocal的student
	local_school.student = name;
	process_student();
	
t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
	