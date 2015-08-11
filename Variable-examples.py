#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Phoenix1327'
a = 'ABC'
b = a
a = 'XYZ'
print(b)

# a --> 'ABC'
# b --> a --> 'ABC'(i.e. b --> 'ABC')
# a --> 'XYZ'

#exercise
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print (n)
print (f)
print (s1)
print (s2)
print (s3)
print (s4)
