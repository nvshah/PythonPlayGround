import struct
from decimal import Decimal

def float_to_bin(f) -> str:
    # d for double precision (64 bit) floating point,
    # > for big-endian (the way we usually write numbers in math)
    fmt = ">d"
    bz = struct.pack(fmt, f)  # <--- MIMP
    print(bz) # bytes obj containing bits according to format string
    return "".join(f"{b:08b}" for b in bz)

def sign_exponent_fraction(s):
    return s[0:1], s[1:12], s[12:64]


def pretty_float_bits(f) -> str:
    return " ".join(sign_exponent_fraction(float_to_bin(f)))


# (1)
# 0.1 + 0.2 == 0.3 ???
print('0.1 :- ', pretty_float_bits(0.1))
print('0.2 :-', pretty_float_bits(0.2))
print('0.3 :-', pretty_float_bits(0.3))
print('0.1 + 0.2 :-', pretty_float_bits(0.1 + 0.2))

''' 
    see 0.3 & 0.1+0.2 differs in decimal part representation
    so 0.1+0.2 is not giving exact 0.3
    As 0.1 & 0.2 is having repeatation in decimal part 
'''

# (2)
# infinite number
x, y = float('inf'), float('inf')
print(x == y, x is y) # True, False

# (3)
# zeros & -zeros
x, y = 0, -0
print(x is y) # True (ie int 0 are same obj irrespective of sign)
x, y = 0., -0.
print(x == y, x is y) # True, False

# (4)
# nan number
''' 
Fact :- nan is the only obj in python that is not comparable ie gives always false
'''
x, y = float('nan'), float('nan')
print(x == y, x is y)  # False, False

#-------------------

# (5)
# Compare 2 floats then take absolute diff & then check it with 10 power
def almost_equal(x, y, eps=10 ** -6):
    return abs(x - y) < eps

# (6)
# Use Decimal Object if wanted exact representation


