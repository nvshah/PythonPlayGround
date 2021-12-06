import math
# Recursive Approach
from typing import List
import functools as ft

from utils_handy import get_digits

# 1
def isArmStrong(n):
    '''
    Armstrong number is a number that is equal to the sum of cubes of its digits
    '''
    def _app1(n):
        n_s = str(n)
        t = sum(map(lambda e: int(e) ** 3, n_s))
        return t == n

    def _app2(n):
        return n == sum(get_digits(n, lambda x: x**3))

    return _app2(n)

# 2
def isPrime(n):
    ''':var
    Goal -> sqrt(n) ?? -> a larger factor of n must be a multiple of smaller factor that has been already checked.
    Also 2 & 3 are only consecutive prime numbers, so
    Any num can be either divide by {1, itself, 2, 3}
    '''
    if n < 3:
        return True

    def _app1():
        # Square Root Range
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    def _app2():
        # Square Range
        c = 2
        while c * c <= n:
            if n % c == 0:
                return False
            c += 1
        return True

    return _app1()

def getdigits(n, func=None):
    '''
    return generator of digits
    if func provided then digit is mapped to that func & then returned
    '''
    while n != 0:
        n, r = divmod(n, 10)
        yield func(r) if func else r

# 3 (MIMP)
def getDigitsCount(n):
    num = abs(n)  # Negative number & positive number going to have same digits count

    def _app1(n):
        '''
        NOTE -> this approach may fail sometimes !!
               (Why ??) -> because floating point are not accurately represented by Computers
               Eg n = 99999999999999997  -> will fail
        '''
        # Max val represented by n digits in 10^n - 1, So we are adding +1 at the end
        # return int(math.log(n, 10)) + 1
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

    def _app4(n):
        '''Plain logic impl of _app1()'''
        tn = abs(n)  # -n if n < 0 else n
        cntr = 1
        while tn >= 10**cntr:
            cntr += 1
        return cntr

    def _app5(n):
        return len(list(getdigits(n)))

    return _app5(num)

def sumOfDigits(n):

    def _app1(n):
        s = 0
        while n:
            q, r = divmod(n, 10)
            n, s = q, s+r
        return s

    def _app2(n):
        if n == 0:
            return 0
        q, r = divmod(n, 10)
        return r + _app2(q)

    def _app3(n):
        return sum(getdigits(n))

    return _app2(n)

# 4
def isEven(n):
    def _app1(n):
        return n | 1 > n

    def _app2(n):
        return not (n & 1)

    def _app3(n):
        return not (n % 2)

    return _app1(abs(n))  # Even will remain even regardless of negative or positive

# 5
def isPalindrome(x: int) -> bool:
    if x < 0: return False  # all negative nums will not be a palindrom as of `-` sign
    t_x = x                 # temp variable for x
    i = r_x = 0             # r_x is to hold reversed number
    while t_x > 0:
        t_x, m = divmod(t_x, 10)
        r_x = r_x * 10 + m
        i += 1
    return x == r_x

def isPalindromeStr(x: str) -> bool:
    assert x, 'Empty String !!!'
    x = x.lower()
    for i in range(len(x) // 2):
        if x[i] != x[-1-i]:
            return False
    return True

def min_max_item_indices(l):
    '''return tuple :- (min_idx, max_idx)'''
    size = len(l)
    b_i = max(range(size), key=l.__getitem__)
    s_i = min(range(size), key=l.__getitem__)

    # b2 = min(range(len(l)), key=lambda x: op.methodcaller('__getitem__', x)(l))
    # b1 = max(range(len(l)), key=lambda x: op.methodcaller('__getitem__', x)(l))

    return (s_i, b_i)  # (min_idx, max_idx)

def permutation(l: List[int]):
    '''
    Find Permutation using Recurssion  # Complexity -> O(n!)
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

    # base (boundary) Case i.e when to select = 1 => select all
    if r == 1:
        return [[e] for e in l]
    if len(l) == r:
        return [l]

    ans = []

    for i in range(len(l)-r+1):
        rest_comb = combination(l[i+1:], r-1)
        ans.extend([[l[i], *c] for c in rest_comb])

    return ans

def doTransposeOf(mat):
    '''
    Inplace Transpose i.e m[i][j] = m[j][i]
    '''
    r = len(mat)
    for i in range(r-1):
        for j in range(i+1, r):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j] # Swap

def transposeOf(mat):
    '''
    Non inplace
    '''
    def a1():
        col_count = len(mat[0])
        row_count = len(mat)
        return [[mat[j][i] for j in range(row_count)] for i in range(col_count)]

    def a2():  # Best 1 Liner
        return zip(*mat) # Transpose of a matrix

def reverseBy2Pointer(l):
    '''inplace - reverse a list'''
    for i in range(len(l) // 2):
        l[i], l[-i-1] = l[-i-1], l[i]  # Swap
    return l

# --- Recursion ---

def gcd(a, b):
    '''Eucledian Algo to find HCF '''
    a, b = min(a,b), max(a,b)
    if not a:   # boundary case
        return b
    return gcd(a, b % a)  # recursive case

def factorial(n):
    assert n > 0, "n must be 0 or +ve"
    if n <= 1:    # boundary case
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    '''find the nth fibonacci number '''
    def a1(n):
        '''recursive approach'''
        return n-1 if n <= 1 else a1(n-1) + a1(n-2)

    def a2(n):
        '''(2 pointer method)'''
        if n <= 1:
            return n-1
        a, b = 0, 1
        for _ in range(n-2):
            a, b = b, a+b
        return b

    @ft.cache
    def fib(n):
        print('calculating fib for: ', n)
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)

def babylonian_sqrt(num):
    '''
    Find the math.isqrt() via babylonian method of approximation
    '''

    def find_floor(arr, t):
        '''return the index of element (assuming index start from 1)'''
        s, e = 0, len(arr)-1
        while s <= e:
            m = s + (e - s) //2
            if t > arr[m]:
                s = m + 1
            elif t < arr[m]:
                e = m - 1
            else:
                return m + 1
        return e + 1

    def speculate_initial_val(n):
        '''
        The Rule of Twos and Sevens chooses an initial guess from among the candidates {2, 7, 20, 70, 200, 700, ...}
        '''
        zeros = pow(10, len(str(n)) // 2)
        l, u = 2 * zeros, 7 * zeros
        l_squared, u_squared = 4 * zeros, 49 * zeros
        m = l_squared + (u_squared-l_squared) // 2  # closeness|proximity decision
        i = l if n < m else u # initial val
        return i

    if num < 225:
        sqs = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
        return find_floor(sqs, num)

    i = speculate_initial_val(num)
    #print('Initial : ', i)
    # find the initial val
    while True:
        #b = round((i + num / i) / 2, decimal_precision)
        #b = floor((i + num / i) / 2)
        b = (i + num / i) / 2
        #print('-> ', b)
        if math.floor(i) == math.floor(b):
            return math.floor(i)
        else:
            i = b

def isqrt(n):
    '''
    math.isqrt() via Binary Search

    Logic ->

    Let's consider
    number - n, divisor - d

    if d divides n into exact d parts then we can say that d is exact square root of n
    if d divides n into more than d parts so -> need to lower the divider
    if d divides n into less than d parts sp -> need to increase the divider
    '''
    s, e = 1, n
    while s <= e:
        m = s + (e-s) // 2
        q = n // m
        if m == q:
            # d divides n into exact d parts, i.e found exact square root
            return m
        elif q > m:
            # d divides n into more than d parts, i.e more parts than expected so increase the divider
            s = m+1
        else:
            # d divides n into less than d parts i.e less parts than expected so decrease the divider
            e = m-1
    return e

if __name__ == '__main__':
    # for i in range(100, 1000):
    # print(isArmStrong(0))
    #
    # print(getDigitsCount(-101))
    #
    #
    # l = [1,2, 3]
    # p = permutation(l)
    # print(p)
    print(babylonian_sqrt(100))

    print(isPalindromeStr('racecar'))  # True

    print(sumOfDigits(1223))
