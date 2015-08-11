#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Phoenix1327'
s = "包含中文的str"
print(s)
print(ord('中'))

#exercise
s1 = 72
s2 = 85

r = (s2 - s1) / s1 * 100
print(r)
print('%.1f%%' % r)