# 1 ---------------------------------------------------
'''
globals() -> returns the reference to global namespace
locals()  -> returns the copy of local namespace
'''

def f1():
    a = 30
    locals()['a'] = 300  # this will not modify local variable a
    return a

a = 10
globals()['a'] = 100 #  modified global variable a

print(a)   # 100
ans = f1()
print(ans)  # 30


# 2-------------------------------------
def test():
    global x  # Even though this x not exists it will be added into global namespace
    x = 150

test()
print(x) # 150


# 3 builtins ----------------------------------

import builtins
print(dir(builtins)) # print the builtin scope i.e names pre-defined by python