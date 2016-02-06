# -*- coding: utf-8 -*-
"""
Week 1 task assignment
"""

class ListDivideException(Exception):
        """Raise Exception"""


def listDivide(numbers, divide=2):
    count = 0
    for x in numbers:
        if x % divide == 0:
            count += 1
    return count


def testListDivide():
    a = listDivide([1,2,3,4,5])
    b = listDivide([2,4,6,8,10])
    c = listDivide([30,54,63,98,100], divide=10)
    d = listDivide([])
    e = listDivide([1,2,3,4,5], 1)

    while a == 2 and b == 5 and c == 2 and d == 0 and e == 5:
        continue
    else:
        raise ListDivideException('Exception: data error')