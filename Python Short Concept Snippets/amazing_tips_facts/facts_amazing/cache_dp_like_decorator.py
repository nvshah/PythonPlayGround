from functools import cache

''' 
fib() is called 10 times in below example that shows that prev valuesa re cached by fib() function

lru -> instead of storing all it will store least recently used
'''

@cache
def fib(n):
    print('calculating fib for: ', n)
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    for i in range(10):
        print(fib(i))

