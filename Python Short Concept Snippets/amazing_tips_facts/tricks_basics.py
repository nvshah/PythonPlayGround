import itertools as it

# Swap using Multiple assignments
w, h = 10, 20  # multiple assignments
w, h = h, w # swap using multiple assignments

# *args
l = [1,2,3]

print(l)
print(*l)

# compress
nums = [1,2,3,4,5]
pick = [1,0,1,0,1]

selected = it.compress(nums, pick)
print(list(selected)) # [1,3,5]

# Chained Comparision

x, y, z = 1, 2, 1
print( x != y != z)  # still x & z are equal

# List to Tuple

t = (*[1,2,3],)  # (1,2,3)