from math import isqrt
from itertools import compress

def prime_less_than(n):
    '''return prime number less thann n
        using SIEVE OF ERANTOSTHESIS
    '''
    if n<=2:
        return []

    # define boolean array to track all elements which are prime or not upto n
    isPrime = [True] * n
    isPrime[0] = False
    isPrime[1] = False

    for i in range(2, isqrt(n)):
        if isPrime[i]: # check for all prime numbers
            # multiple of all prime numbers are non-prime
            for x in range(i*i, n, i): # prime number found using only i at moment
                isPrime[x] = False

    #return [i for i in range(n) if isPrime[i]]
    return compress(range(n), isPrime)

if __name__ == '__main__':
    n = 30
    a1 = [*prime_less_than(n)]
    print(a1)
