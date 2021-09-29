import math
# Recursive Approach
from typing import List

def isArmStrong(n):
    '''
    Armstrong number is a number that is equal to the sum of cubes of its digits
    '''
    n_s = str(n)
    t = sum(map(lambda e: int(e) ** 3, n_s))
    return t == n


def isPrime(n):
    ''':var
    Goal -> sqrt(n) ?? -> a larger factor of n must be a multiple of smaller factor that has been already checked.
    Also 2 & 3 are only consecutive prime numbers, so
    Any num can be either divide by {1, itself, 2, 3}
    '''
    if n < 1:
        return n

    def _app1():
        # Square Root Range
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return True

    def _app2():
        # Square Range
        c = 2
        while c * c <= n:
            if n % c == 0:
                return True
            c += 1

    return _app1()


def getDigitsCount(n):
    num = abs(n)  # Negative number & positive number going to have same digits count

    def _app1(n):
        # Max val represented by n digits in 10^n - 1, So we are adding +1 at the end
        return math.floor(math.log(n, 10)) + 1

    def _app2(n):
        if n == 0:
            return 1
        else:
            ctr = 0
            while n > 0:
                n //= 10
                ctr += 1
            return ctr

    def _app3(n):
        return len(str(n))

    return _app1(num)


def isEven(n):
    def _app1(n):
        return n | 1 > n

    def _app2(n):
        return not (n & 1)

    def _app3(n):
        return not (n % 2)

    return _app1(abs(n))  # Even will remain even regardless of negative or positive

# Complexity -> O(n!)
def permutation(l: List[int]):
    '''
    Find Permutation using Recurssion
    :param: l -> list
    :return: -> all permutations i.e npn
    '''
    # Base Case -> At Most 1 element
    if len(l) <= 1:
        return [l]
    ans = []
    # indxd_l = list(enumerate(l))

    # for i in range(len(l)):
    #     fix_i = [e for j, e in indxd_l if j!=i]
    #     perm_rest = permutation(fix_i)
    #     ans.extend(([l[i], *p] for p in perm_rest))
    for e in l:
        fix_e = [i for i in l if e != i]
        perm_rest = permutation(fix_e)
        ans.extend(([e, *p] for p in perm_rest))
    return ans

def combination(l, r):
    '''
    Find Combination using Recurrsion
     :param : l -> list
     :r : r -> num of elements to pick
    '''
    assert len(l) >= r, "Length of l must be >= r"

    # base Case i.e when to select = 1 => select all
    if r == 1:
        return [[e] for e in l]
    if len(l) == r:
        return [l]

    ans = []

    for i in range(len(l)-r+1):
        rest_comb = combination(l[i+1:], r-1)
        ans.extend([[l[i], *c] for c in rest_comb])

    return ans




if __name__ == '__main__':
    # for i in range(100, 1000):
    print(isArmStrong(0))

    print(getDigitsCount(-101))


    l = [1,2, 3]
    p = permutation(l)
    print(p)
