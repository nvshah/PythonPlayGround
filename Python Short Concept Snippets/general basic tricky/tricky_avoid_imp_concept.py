# 1 ---------------------------------
# Avoid passing default param value to be mutable
'''
NOTE -> default value is assigned only once when function object is created
        i.e during definition time.
        Verify -> by checking `id` of p2 param in each function call, it will remain same every time
'''

def f1(p1, p2=[0]):
    print(id(p2))  # Id will remain same despite no. of function calls
    p2.append(p1)
    print(p2)

def f2(p1, p2=(0,)):
    print(id(p2))   # Id will remain same despite no. of function calls
    p2 = p2 + (p1,)
    print(p2)

f1(10)
f1(20)

f2(10)
f2(20)

# 2 -------------------------------------
# use `defaultdict` whenever it fits
from collections import  defaultdict

nums = [1,2,3,4,4,5,5,6]
count = defaultdict(int)  # defaultdict(lambda: 0)
for n in nums:
    count[n] += 1
print(count)  # ... {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 1} ...

# 3 ------------------------------------
# utilise `setdefault` whenever if fits

d1 = {1:1, 2:2}
d1.setdefault(3, []).append(10)
print(d1)  # {1: 1, 2: 2, 3: [10]}

