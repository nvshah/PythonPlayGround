import math

def squares(n):
    for i in range(1,n+1):
        yield i**2

sq_1_5 = squares(5)
e_sq = enumerate(sq_1_5)

next(sq_1_5)
next(sq_1_5)

print(list(e_sq))  # [(0, 9), (1, 16), (2, 25)]

