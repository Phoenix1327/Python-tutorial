#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Phoenix1327'

def normalize(name):
    return name[0].upper() + name.lower()[1:]

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


from functools import reduce
def mul(x, y):
    return x * y
def prod(L):
    return reduce(mul, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def str2float(s):
    n = s.find('.')
    s = (n == -1) and s or s[:n] + s[n+1:]
    if n == -1:
        n = 0
    print(n)
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s)) / 10**n

print('str2float(\'123.456\') =', str2float('123.456'))