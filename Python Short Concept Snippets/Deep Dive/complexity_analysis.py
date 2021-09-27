import tracemalloc
from math import factorial as fact
from timeit import timeit

def combo(n, k):
    return fact(n) // (fact(k) * fact(n-k))

def pascal_list(size):
    l = [[combo(n, k) for k in range(n+1)] for n in range(size+1)]
    for row in l:
        for item in row:
            pass
    # Putting here at the end of function line as may be after function call gets ended
    #  resources may get released so we won't get idea about memory being taken by `l` over here
    stats =  tracemalloc.take_snapshot().statistics('lineno')
    print(stats[0].size, 'bytes')

def pascal_gen(size):
    l = ([combo(n, k) for k in range(n+1)] for n in range(size+1))
    for row in l:
        for item in row:
            pass
    # Putting here at the end of function line as may be after function call gets ended
    #  resources may get released so we won't get idea about memory being taken by `l` over here
    stats =  tracemalloc.take_snapshot().statistics('lineno')
    print(stats[0].size, 'bytes')

size = 600

#-1--- Time Complexity----
timeit('pascal_list(size)', globals=globals(), number=1)
timeit('pascal_gen(size)', globals=globals(), number=1)

#-2---- Space Complexity

tracemalloc.stop()
tracemalloc.clear_traces()
tracemalloc.start()
pascal_list(300) # more bytes
pascal_gen(300) # less bytes comparatively


