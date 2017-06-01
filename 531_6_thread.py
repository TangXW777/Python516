#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

##============ 线程 ===============
#import time, threading
#
## 新线程执行的代码:
#def loop():
#    print('thread %s is running...' % threading.current_thread().name)
#    n = 0
#    while n < 5:
#        n = n + 1
#        print('thread %s >>> %s' % (threading.current_thread().name, n))
#        time.sleep(1)
#    print('thread %s ended.' % threading.current_thread().name)
#
#print('thread %s is running...' % threading.current_thread().name)
#t = threading.Thread(target=loop, name='LoopThread')
#t.start()
#t.join()
#print('thread %s ended.' % threading.current_thread().name)

##多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
##所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改.

#import time, threading
#balance = 0;
#def change_it(n):
#	global balance
#	balance = balance + n;
#	balance = balance - n;
#	
#def run_thread(n):
#	for i in range(1000000):
#		change_it(n);
#
#t1 = threading.Thread(target=run_thread, args=(5,));
#t2 = threading.Thread(target=run_thread, args=(8,));
#t1.start();
#t2.start();
#t1.join();
#t2.join();
#print(balance);

## 上面的运算结果发现并一定为0，因为t1,t2交替执行
## 所以需要给balance加锁，保证每次只有一个change_it()

import time, threading
balance = 0;
lock = threading.Lock();
def change_it(n):
	global balance
	balance = balance + n;
	balance = balance - n;
	
def run_thread(n):
	for i in range(1000000):
		## 获取锁
		lock.acquire();
		try:
			change_it(n);
		finally:
			## 改好释放锁
			lock.release();

t1 = threading.Thread(target=run_thread, args=(5,));
t2 = threading.Thread(target=run_thread, args=(8,));
t1.start();
t2.start();
t1.join();
t2.join();
print(balance);

## 上面运算结果为0，因为加锁，但是运算速度也相对变慢
