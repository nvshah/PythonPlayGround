from numbers import Number

# Predicate
def is_numeric(o):
    return isinstance(o, Number)

l = [10, 20, '20', 30, 40, 0]
pred_l = map(is_numeric, l)

print(all(pred_l)) # False