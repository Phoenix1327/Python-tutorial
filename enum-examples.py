#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

from enum import Enum, unique

Month = Enum('enum_Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print(Month)
print(Month.Jan)
print(Month.Jan.name)
print(Month.Jan.value)

@unique
class Weekday(Enum):
    Sun = 0#从0开始，Enum默认从1开始
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
