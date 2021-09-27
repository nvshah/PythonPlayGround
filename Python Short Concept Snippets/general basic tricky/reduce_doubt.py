from functools import reduce
from math import prod

n = [1, 2, 3]

#a = reduce(prod, n, initial=10)
#print(a)
_a = 10

def f_from(a, b=_a):
    print(a, b)
