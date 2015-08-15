#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Administrator'


def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    output = filter(is_palindrome, range(1,1000))
    print(list(output))
