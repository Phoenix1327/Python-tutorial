#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

import functools

def log(text='execute'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call')
            print('%s call %s():' % (text, func.__name__))
            func(*args, **kw)
            print('end call')
        return wrapper
    return  decorator

@log('execute')
def now():
    print('2015')

now()
