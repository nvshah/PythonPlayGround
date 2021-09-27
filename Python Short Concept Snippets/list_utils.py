import operator
from collections import Counter as ctr
from typing import List
import itertools as it


def canEitherListBeEaten(l1: list, l2: list):
    '''
        Check if l1's elements all are presented in l2's element
    '''
    len_l1 = len(l1)
    len_l2 = len(l2)

    if len_l1 > len_l2:
        s, b = l2, l1
    else:
        s, b = l1, l2

    for e in s:
        if s.count(e) > b.count(e):
            break
    else:
        return True
    return False


# Approach 1 (In-Place) , Works only with list
def join_inplace(itr: List, filler: object) -> List:
    '''O(1) space Complexity
       O(n^2) time complexity
    '''
    if len(itr) == 1:
        return itr
    for i in range(len(itr) - 1, 0, -1):
        itr.insert(i, filler)


def join(itr: List, filler: object) -> List:
    '''
      O(n) time complexity
      O(2n) space complexity
    '''
    l = len(itr)
    if l == 1:
        return itr
    return [itr[i // 2] if i % 2 else filler for i in range(1, l * 2)]


# Approach 3, Works with any iterable
def join2(itr, filler):
    return [*it.chain.from_iterable(t for t in zip(itr, it.repeat(filler, len(itr) - 1)))] + itr[-1:]


def count(nums, toAccount):
    ctr = 0
    for n in nums:
        if toAccount(n):
            ctr += 1
    return  ctr



if __name__ == '__main__':
    s = canEitherListBeEaten([13, 12, 2], [2, 2, 12, 13])
    print(s)

    l1 = [1, 2, 3, 4]
    l2 = [1, 2, 4, 5]

    join_inplace(l1, '-')
    m = join(l2, '*')
    a = join2(l2, '/')
    print(l1)

    print(m)
    print(a)
