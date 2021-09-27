t1 = tuple(i for i in range(5))  # Note here used comprehension directly as argument of tuple

print(t1) #(0,1,2,3,4)

import sys
'''
 Tuple also implement canonicalization using 
'''

# 8 bits - 1 byte upto elements can get interned by the tuple
t1 = (1,)*256
t2 = (1,)*256

print(t1 is t2, t1 == t2)