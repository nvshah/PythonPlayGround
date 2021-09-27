### 1. --------------------------------------
# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted(xs.items(), key=lambda x: x[1])
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

import operator

sorted(xs.items(), key=operator.itemgetter(1))
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

### 2. --------------------------------------
# Merge 2 dict into 1

d1 = {1: 1, 2: 2, 3: 3}
d2 = {3: 30, 4: 4, 5: 5}
d3 = {**d1, **d2}

### 3. Turn 2 seperate List into dictionary  -------------

l1 = [1, 2, 3, 4, 5]  # keys
l2 = ['1', '2', '3', '4', '5']  # values

d = dict(zip(l1, l2))

print(d)

### 4 IMP Trick --------------------
# Use dictionary comprehension with zip() most of time to get elegant soln for filtering

l1 = [1, 2, 3, 34]
l2 = ['one', 'two', 'three', 'thirty-four']

d = {k: v for k, v in zip(l1, l2) if not (k & 1)}  # Even Filter Pairs

print(d)

### 5 Get the first value or key in dict ------

d = {1:1, 2:2, 3:3, 4:4}
first_item = next(iter(d.items())) # (1, 1)
first_key = first_item[0]  # 1
first_val = first_item[1]  # 1

print(first_item, first_key, first_val) # (1, 1) 1 1
