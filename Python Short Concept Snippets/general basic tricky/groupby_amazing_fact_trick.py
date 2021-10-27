from itertools import groupby

l = [1,1,1,2,2,2,3,3,3,1,1,2,2,4,4,4,5,5]
ln = sorted(l)
g = iter(l)  # iterator
packed = groupby(g)  # uses actual g underhood

for k, v in packed:
    print(k, list(v))

''' OUTPUT
1 [1, 1, 1]
2 [2, 2, 2]
3 [3, 3, 3]
1 [1, 1]
2 [2, 2]
4 [4, 4, 4]
5 [5, 5]
'''
print(list(g)) # []  // Empty as its consumed by groupby actually


