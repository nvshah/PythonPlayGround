#Interning
# ref -> https://medium.com/@bdov_/https-medium-com-bdov-python-objects-part-iii-string-interning-625d3c7319de

a = "".join(["H", "e", "l", "l", "o"])  # run time
b = "H"+"e"+"l"+"l"+"o"  # compile time
c = "Hello"              # compile time

print(a is b, a is c, b is c) # False False True

# 1. Walrus
def f(num):
    return num + 1

if (x := f(20)) > 20:
    print(x)


# 2
a = "Hello"
b = "".join(["H", "e", "l", "l", "o"])
c = "H" + "e" + "l" + "l" + "o"
print(a is b, a is c, b is c)


# 3 bool & int interoperability
print((1 == 1) in [1])  # True
print(1 == (1 in [1]))  # True
print(1 < (0 < 1))  # False
print(1 < 0 < 1)  # equi to print((1<0) and (0<1))

# 4 Hashing (Constant Lookup & Const deletion)
d = {}
d[1] = "1"
d[1.0] = "2"
d[2 - 1] = "3"
print(d)
print(hash(1), hash(1.0), hash(2 - 1), hash(True))  # all are same

# 5 Nested list = false
print(all([1, 2, []]))  # false
print(all([1, 2, [[]]]))  # true


#6 not and ==  [== has higher precedence than not]
x = True
y = False
print(not x == y)
# print(x == not y) # Error expected an expression
print(x == (not y))


# 7 Circular reference
a, b = a[b] = {}, 5
print(a)  # {5: ({...}, 5)}
print(b)
"""
    first ->
       a, b = {}, 5
    second -> 
       a[b] = {5: ({5: ({5: ()}, 5)}, 5)}  # this go on ...
     So ->
       a[b] = {5: ({...}, 5)}

    {...} deontes the circular reference to same dict object
"""