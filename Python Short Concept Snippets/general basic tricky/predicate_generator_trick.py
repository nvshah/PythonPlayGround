g = (i for i in range(5))

res = all((e < 2 for e in g))  # True

print(*g)  # '3 4'