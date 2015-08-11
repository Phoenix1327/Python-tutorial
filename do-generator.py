#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Phoenix1327'

def triangles():
    yield [1]
    n = 1
    line = [1,1]
    while True:
        yield line
        next_line = [line[x]+line[x+1] for x in range(n)]
        next_line.insert(0, 1)
        next_line.append(1)
        line[:] = next_line[:]
        n += 1

n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break

