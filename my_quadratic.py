#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Phoenix1327'

import math

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b*b - 4*a*c)) / a * 0.5
    x2 = (-b - math.sqrt(b*b - 4*a*c)) / a * 0.5
    return x1, x2

r = quadratic(1, 4, 4)
print(r)
