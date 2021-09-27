import itertools as it

l = [0, 0, 0, 0]


def update(v1, v2):
    l[v1] = v2
    return v1 + v2


acc = it.accumulate(l, func=update)
