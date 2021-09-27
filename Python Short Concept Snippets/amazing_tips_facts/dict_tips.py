d1 = {1: '1', 2: '2', 3: '3'}
d2 = {2: '02', 4: '4', 5: '5'}

# MERGE 2 Dict

# 1. BEST  (>= 3.9)
d3 = d1 | d2
print(d3)

# 2.
d3 = {**d1, **d2}
print(d3)

# 3
d3 = d1.copy()
d3.update(d2)
print(d3)
