import operator
import random
import time
from typing import List, Any
import itertools as it
import functools as ft


''' 
 Flatten  List
 1 liner -> functools.reduce()  +  operator.iconcat()   // is fastest
 general -> `+=` in for loop i.e inplace concatenation
'''

def flatten0(l: List[List[int]]) -> List[int]:  # worst
    l = []
    for i in l:
        for j in i:
            l.append(j)
    return l

def flatten1(l: List[List[int]]) -> List[int]:  # Third-best
    f = []
    for a in l:
        f.extend(a)
    return f

def flatten11(l: List[List[int]]) -> List[int]:  # Best
    f = []
    for a in l:
        f += a  # inplace
    return f

def flatten2(l: List[List[int]]) -> List[int]:  # faster than double for loop but slower otherwise
    return [e for a in l for e in a]


def flatten3(l: List[List[int]]) -> List[int]:  # Average
    return list(it.chain.from_iterable(l))

def flatten4(l: List[List[Any]]) -> List[Any]:  # The Second best
    '''Beautiful way using functools'''
    # `+=`
    return ft.reduce(operator.iconcat, l, [])


def time_f(func):
    elapsed = 0
    n = 100
    M = 1000
    N = 100

    for _ in range(n):
        lst = [[random.randint(1, 100_000) for _ in range(N)] for _ in range(M)]
        start = time.perf_counter()  # Note perf_cntr uses cpu cycles so need second perfcntr to calculate elapsed time
        func(lst)
        end = time.perf_counter()
        elapsed += end - start   # number of seconds
    print(elapsed / n * 1000, 'ms')  # in milli seconds

if __name__ == '__main__':
    l = [[1,2], [3,4], [5,6]]
    print(flatten4(l))   # [1, 2, 3, 4, 5, 6]

    l = [[[1,2], [3,4]], [[5,6], [7,8]]]  # 2 times flattening
    print(flatten4(flatten4(l)))  # [1, 2, 3, 4, 5, 6, 7, 8]

    #time_f(flatten4)
