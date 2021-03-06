#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Administrator'


def fact(n):
    '''
    Return the factorial of an integer, with number of other types it can raise corresponding error

    >>> fact(5)
    120

    >>> fact(1)
    1

    >>> fact(0)
    Traceback (most recent call last):
    ...
    ValueError

    >>> fact('abc')
    Traceback (most recent call last):
    ...
    TypeError: unorderable types: str() < int()
    '''

    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
