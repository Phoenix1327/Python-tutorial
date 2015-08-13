#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

class Chain(object):

    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)

#1.Chain(),调用__init__,path='',得到self._path=''
#2.Chain().status 调用__getattr__('status'),返回Chain('', '/status')，调用__init__('/status')，得到self._path='/status'
#3.Chain().status.user 调用__getattr__('user'),返回Chain('/status', '/user'),调用__init__('/user'),得到self._path='/status/user'
#4 Chain().status.user.timeline 调用__getattr__('timeline'),返回Chain('/status/user', 'timeline'),调用__init__('timeline')，
#  得到self._path='/status/user/timeline'
#5 Chain().status.user.timeline.list.......得到self._path=/status/user/timeline/list
#6 print,调用__str__(),输出/status/user/timeline/list