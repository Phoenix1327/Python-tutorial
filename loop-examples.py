#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Phoenix1327'

sum = 0
for x in range(101):
    sum += x
print(sum)

sum = 0
n = 100
while n > 0:
    sum += n
    n -= 1
print(sum)

#exercise
L = ['Bart', 'Lisa', 'Adam']
for item in L:
    print('Hello, %s!' % item)


#function
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))