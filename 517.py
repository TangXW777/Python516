#!usr/bin/env python3
# -*- encoding: utf-8 -*-
def is_odd(n):
	return n % 2 == 1;
# print(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9]));
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])));

# sorted
# 根据绝对值进行排序
n = sorted([36, 5, -12, 9, -21], key=abs);
print(n);
# 忽略大小写
m = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower);
print(m);
# 反向
s = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True);
print(s);
