#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Phoenix1327'

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')

def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end([1,2,3]))
print(add_end())

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n*n
    return sum

print(calc(1, 2, 3))
nums = [1, 2, 3]
print(calc(*nums))


def move(n, org, via, dst, L):
    if n == 1:
        L.append('# %s - -> %s' % (org, dst))
    else:
        move(n-1, org, dst, via, L)
        move(1, org, via, dst, L)
        move(n-1, via, org, dst, L)

L=[]
move(3, 'A', 'B', 'C', L)
for x, value in enumerate(L):
    print('step:%d %s' % (x+1, value))
