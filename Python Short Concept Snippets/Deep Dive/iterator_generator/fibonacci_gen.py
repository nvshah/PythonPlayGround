def fibo(n):
    fibo_0 = 1
    yield  1
    fibo_1 = 1
    yield 1
    for i in range(n-1):
        fibo_0, fibo_1 = fibo_1, fibo_1 + fibo_0
        yield fibo_1

fib_g = fibo(5)

for n in fib_g:
    print(n)
