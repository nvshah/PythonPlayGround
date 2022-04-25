from functools import cmp_to_key

l = [2, 20, 45, 3, 10, 5, 6, 27, 35]

s1 = sorted(l, key=lambda x: -x)

def m5(n1, n2):
    if -n1 > -n2:
        return 1  # n2
    else:
        return -1  # n1

s2 = sorted(l, key=cmp_to_key(m5))

print(s1)
print(s2)
