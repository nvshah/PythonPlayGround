import math
# Recursive Approach
from typing import List

# 1
def isArmStrong(n):
    '''
    Armstrong number is a number that is equal to the sum of cubes of its digits
    '''
    n_s = str(n)
    t = sum(map(lambda e: int(e) ** 3, n_s))
    return t == n

# 2
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

    return _app4(num)

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
def isPalindrome(self, x: int) -> bool:
    if x < 0: return False  # all negative nums will not be a palindrom as of `-` sign
    t_x = x                 # temp variable for x
    i = r_x = 0             # r_x is to hold reversed number
    while t_x > 0:
        t_x, m = divmod(t_x, 10)
        r_x = r_x * 10 + m
        i += 1
    return x == r_x

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



if __name__ == '__main__':
    # for i in range(100, 1000):
    print(isArmStrong(0))

    print(getDigitsCount(-101))


    l = [1,2, 3]
    p = permutation(l)
    print(p)
