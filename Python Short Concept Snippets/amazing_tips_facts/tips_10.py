import itertools as it

# ----> MODIFY lisT

# Approach 1
import timeit


def even(x):
    return x % 2 == 0

def a1():
    a = [1,2,3,4]
    for e in a[:]:
        if not e % 2:
            a.remove(e)

def a2():
    # BEST APPROACH  (NOT INPLACE MODIFICATIONS)
    a = [1,2,3,4]
    a = [x for x in a if x % 2]

def a3():
    # SECOND BEST (INPLACE Modifications)
    a = [1,2,3,4]
    a[:] = [x for x in a if x % 2]

def a4():
    a = [1,2,3,4]
    a[:] = it.filterfalse(even, a)

print(timeit.timeit(a1, number=10) * 1000)
print(timeit.timeit(a2, number=10) * 1000)
print(timeit.timeit(a3, number=10) * 1000)
print(timeit.timeit(a4, number=10) * 1000)
