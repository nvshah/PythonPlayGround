# all() & generator

g1 = (i for i in [1, 2, 3, 4, 5])
g2 = (i for i in [1, 2, 3, 5, 6])

ans = all(s == t for s, t in zip(g1, g2))

print(ans)  # False
'''
g1 & g2 were not entirely consumed by all(), once any false condition found 
it stop iteration further 
'''
print(*g1, '-<>-', *g2)  # 5 -<>- 6
