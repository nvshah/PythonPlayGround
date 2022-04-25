from math import isqrt

def factors(n):
    '''
    Find the factors of n
    :param n: n
    :return: list of factors of n
    '''
    ans = []
    for i in range(1, isqrt(n)+1):
        d, r = divmod(n, i)
        if r == 0:
            if d == i:
                ans.append(i)
            else:
                ans.extend([i, d])
    return ans

def factors_sorted(n):
    '''
    Find the factors of n
    :param n: n
    :return: list of factors of n in sorted order
    '''
    first = []  # first half of factors
    second = [] # second half of factors
    for i in range(1, isqrt(n)+1):
        d, r = divmod(n, i)
        if r == 0:
            if d == i:
                first.append(i)
            else:
                first.append(i)
                second.append(d)
    return first + second[::-1]

def gcd_euc(a, b):
    '''
    GCD using Eucledian Algo (Iteratively)
    '''
    n1, n2 = max(a,b), min(a,b)
    while True:
        r = n1 % n2
        if r == 0:
            return n2
        n1, n2 = n2, r

def gcd_euc_rec(a, b):
    '''
    GCD using Eucledian Algo (Recurssively)
    '''
    a, b = sorted([a,b])

    def gcd(s, b):
        if s == 0:
            return b
        return gcd(b % s, s)

    return gcd(a, b)


def lcm(a, b):
    return a*b / gcd_euc(a,b)



#print(factors_sorted(6))
print(gcd_euc(8, 20))