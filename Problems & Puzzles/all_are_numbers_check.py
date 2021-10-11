from numbers import Number

l = [1, '1', True]

print(all(isinstance(i, Number) for i in l))  # False