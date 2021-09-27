from dis import dis

def f1(x):
    return x * 1 // 2

def f2(x):
    return x * (1 // 2)

print('start')
print(dis(f1))   # underhood less instructions are required hence fast i.e #4

print(dis(f2))   # underhood more instructions are required hence slow i.e #7

print('ds')