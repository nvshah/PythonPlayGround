# NORMAL FUNCTION ------------------------
def f1(n):
    def fi():
        print(n)  # n is a free variable
    return fi

nos = '1', '2', '3'
funcs = []

for n in nos:
    funcs.append(f1(n)) # Here n is bound to function at compile time kinda thing

# 1 2 3
for f in funcs:
    f()

# LAMBDA FUNCTION (Tricky issue) --------------------------------

nos = '1', '2', '3'
funcs = []

for n in nos:
    funcs.append(lambda: print(n)) # Here free variable n will be bound at run time so

# 3 3 3
for f in funcs:
    f()

# Mitigate Above Lambda Closure Issue ----------------------------

nos = '1', '2', '3'
funcs = []

for n in nos:
    #lambda function can assign default value to parameters
    funcs.append(lambda n=n: print(n)) # Here free variable n will be bound at compile(definition) time so

# 1 2 3
for f in funcs:
    f()

