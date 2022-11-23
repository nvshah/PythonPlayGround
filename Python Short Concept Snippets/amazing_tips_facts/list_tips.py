import operator
import functools as ft
from typing import List

# List Concatenation Non-Inplace
l1 = [1,2,3,4]
l2 = [5,6,7]

#1.
l3 = [*l1,*l2]

#2.
l3 = l1 + l2

# functools + Operator -------------------------
def flatten_list(l: List[List[int]])->List[int]:
    return ft.reduce(operator.iconcat, l, [])


# `+=` List amazing concept -------------

a = [1,2]
print(id(a))  # 140614303925184
b = a
a += [4, 5]   # += is inplace concat i.e iconcat()
print(id(a))  # 140614303925184  same as above
b.append(10)
print(a)     # [1, 2, 4, 5, 10]

# 