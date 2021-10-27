from collections import deque
import functools
from typing import Deque
import itertools as it

def fibonacci_a1(length):
    '''
    Recursive approach
    '''
    s1 = 0
    s2 = 1
    left = max(0,(length - 2))

    def inner_fibonacci(secondLast, last):
        nonlocal left
        if left:
            newlast = secondLast + last
            left -= 1
            return [newlast, *inner_fibonacci(last, newlast)]
        else:
            return []

    if length == 1:
        return [s1]
    elif length == 2:
        return [s1, s2]
    else:
        return [s1, s2, *inner_fibonacci(s1, s2)]

def fibonacci_a2(length):
    '''
    Dynamic Programming using lru cache instead of dictionary for memoizing
    '''
    if length == 0:
        return [0]
    if length == 1:
        return [0, 1]

    l = [0, 1]

    @functools.lru_cache(maxsize=128)
    def fibonacci_dp(n):
        if n<=1:
            return n
        nextV = fibonacci_dp(n-1) + fibonacci_dp(n-2)
        l.append(nextV)
        return nextV #Just inorder to cache value

    fibonacci_dp(length)
    return l

def fibonacci_a3(length):
    '''
    remember only last 2 value
    '''
    n = 1
    sn = 0

    if length <= 1:
        return [0, 1] if length else [0]
    lv = 0
    return list(it.accumulate([0, 1, *[0]*(length-2)], lambda x, y, : [print(x, y, lv),locals().update(lv=x), x+y][2]))

@functools.cache
def fib(n):
    print('calculating fib for: ', n)
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    #series = fibonacci_a1(2)
    #series = fibonacci_a2(5)

    #print(series)

    s = fibonacci_a3(5)
    print(s)



