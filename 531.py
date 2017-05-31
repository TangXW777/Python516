#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

##=========== 调试错误 ================

##============= 1.print ==============
##============= 2.断言 ==============
#def foo(s):
#	n = int(s);
#	assert n != 0, 'n is zero!';
#	return 10 / n;
#	
#def main():
#	foo('0');
## 启动Python解释器时可以用-O参数来关闭assert


##============= 3.logging ================
#import logging
#logging.basicConfig(level=logging.INFO)
#s = '0';
#n = int(s);
#logging.info('n = %d' %n);
#print(10 / n);


##============= 4.pdb调试 启动时加参数-m pdb =========================
## l查看代码 n但不执行 p x查看变量 q停止调试
#s = '0';
#n = int(s);
#print(10 / n);



##============ pdb.set_trace() ==================
import pdb

s = '0';
n = int(s);
pdb.set_trace() ## 运行到这里会自动暂停
print(10 / n);