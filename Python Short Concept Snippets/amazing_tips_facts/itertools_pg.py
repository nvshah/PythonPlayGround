import itertools as it

# 1 --- Accumulate
l = [0, 0, 0, 0]
def update(v1, v2):
    l[v1] = v2
    return v1 + v2
acc = it.accumulate(l, func=update)


# 2 ---- generate with step size of float
l = it.count(3, 0.5)  # -> returns iterator so no need to call iter()
l2 = [next(l) for _ in range(3)]

print(l2)  # [3, 3.5, 4.0]

# Much more concise Way of above Equivalent ( count() + islice() )
l = it.count(3, 0.5)
print(*it.islice(l, 3))  # 3 3.5 4.0   //Equivalent ob above but much concise way
