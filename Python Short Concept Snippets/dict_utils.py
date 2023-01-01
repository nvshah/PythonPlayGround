# dict_utils

from collections import defaultdict
from itertools import count

def dict_from_keys_values(keys, values):
    return dict(zip(keys, values))


def default_dict_incrementer():
    '''default dict that assigns default value in an increment fashion
       concepts includes :- Closure & Free variables
    '''
    cntr = it.count()
    incrementer = ct.defaultdict(cntr.__next__)
    return incrementer
