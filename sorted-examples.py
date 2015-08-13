#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return str.lower(t[0])

L2 = sorted(L, key=by_name)
print(L2)