#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Phoenix1327'

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[-1])

classmates.insert(1, 'Jack')
print(classmates)

print(classmates.pop())
print(classmates)

print(classmates.pop(1))
print(classmates)

classmates[1] = 'Sarah'
print(classmates)

#exercise1
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

#exercise2
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() if isinstance(s, str) else s for s in L1]
L3 = [s.lower() for s in L1 if isinstance(s, str)]
#如果需要if else, if else写在for的前面
#如果只需要if, if写在for的后面
print(L2)
print(L3)