from functools import reduce
from operator import xor
from math import log2

'''
range format for n bits :- -2^n-1 -> 2^n-1 - 1

'''

def isOdd(n):
    return bool(n & 1)

def findUnique(arr):
    ''' return element that has count/freq = 1
        NOTE : only 1 element cnt = 1
               all rest element cnt = Even times
    '''
    return reduce(xor, arr)

def find_ith_bit(n, i):
    ''' bit number start from 1 & its accounted from LSB -> MSB '''
    return 1 if n & (1 << i-1) else 0

def set_ith_bit(n, i):
    return n | (1 << i-1)

def reset_ith_bit(n, i):
    return n & (not (1 << n-1))

def cnt_bits(n):
    return int(log2(n)) + 1

def sum_of_nth_row_pascal_triangle(n):
    ''' 2^n-1 for nth row of row starts from 0 '''
    return 1 << n-1  # pow(2, n-1)

def get_binary_repr(n):
    return format(n, '0b')

def is_num_in_power_of_2(n):
    if n == 0:
        return False
    return (n & n-1) == 0
    #bits_len = n.bit_length()
    #print(bits_len)
    #return (log2(n) % 1) == 0  # extract decimal part
    #return not bool(n & (pow(2, bits_len-1) - 1)) # and with 1 bit less

def power(a, b):
    ans = 1
    while b > 0 :
        if b & 1:
            ans *= a
        a *= a
        b = b >> 1
    return ans

def get_set_bits_cnt(n):
    def _app1(n):
        ''' Logic rshift + modulo
            Set bits in a number are also called as Hamming Weight of a number
        '''
        ans = 0
        while n:
            ans += n%2
            #n = n // 10 # shift right i.e discard last bit|number
            n >>= 1
        return ans

    def _app2(n):
        cnt = 0
        while n > 0:
            cnt += 1
            n -= n & -n  # discard rhs set bit
        return cnt

    def _app3(n):
        cnt = 0
        while n > 0:
            cnt += 1
            n = n & (n-1)

    return _app3(n)


def rhs_set_bit(n):
    ''' -n is in 2's complement  '''
    return n & -n

# -> RANGE XOR

def xor_0_to_n(n):
    ''' calculate XOR of 0 to n '''
    mod = n % 4
    if mod == 0:
        return n
    if mod == 1:
        return 1
    if mod == 2:
        return n+1
    #if mod == 3:
    return 0

def xor_a_to_b(a, b):
    ''' calculate xor from a -> b '''
    return xor_0_to_n(b) ^ xor_0_to_n(a-1)



if __name__ == '__main__':
    l = [1,2,4,2,4,1,6,5,3,3,5]
    print(findUnique(l)) # 6

    n = 12
    print(find_ith_bit(n, 1))

    print(is_num_in_power_of_2(9))
