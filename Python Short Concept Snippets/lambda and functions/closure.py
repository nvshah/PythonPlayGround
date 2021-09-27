def outer_func(x):
    y = 4
    #inner func will capture x & y
    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z
    return inner_func

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")


#------------------ LAMBDA & Closure

def outer_func_l(x):
    y = 4
    return lambda z: x + y + z

for i in range(3):
    closure = outer_func_l(i)
    print(f"closure({i+5}) = {closure(i+5)}")