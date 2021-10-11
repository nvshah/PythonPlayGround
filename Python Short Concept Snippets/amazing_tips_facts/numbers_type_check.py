'''
AIM -> check if any kind of number is belonging to number family
'''

from numbers import Number
from decimal import Decimal


l = [1, '1', 1.0, True, 'Haha', 1+2j, Decimal('10.2')]

nums = [i for i in l if isinstance(i, Number)]

print(nums)  # [1, 1.0, True, (1+2j)]