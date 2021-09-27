import math


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


if __name__ == '__main__':
    # for i in range(100, 1000):
    print(isArmStrong(0))

    print(getDigitsCount(-101))
