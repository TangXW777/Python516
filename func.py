#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

def getName(name):
	return name[0:1].upper() + name[1:].lower();

namelist = ['adam', 'LISA', 'barT'];
namemap = map(getName, namelist);
print(list(namemap));

def getResult(x, y):
	return x * y;
numlist = [1, 3, 5, 7, 9];
results = reduce(getResult, numlist);
print(results);

def str2float(s):
    n=10**-(s[::-1].index('.'))
    print(s[::-1]);
    return int(s[:s.index('.')]) + int(s[s.index('.')+1:])*n
floatnum = str2float('12434334.234423456');
print(floatnum);

print(list(map(int,'123456')))