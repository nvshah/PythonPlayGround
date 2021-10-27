def hammingWeight(n: int) -> int:
    '''
    Hamming weight counts the number of 1 in binary form of number n
    '''
    def _app1(n):
        '''Logic :- discarding 1 each time 1 by one & counting'''
        ans = 0
        while n:
            n &= (n-1)
            ans += 1
        return ans

    def _app2(n):
        '''Logic :- rshift + modulo'''
        ans = 0
        while n:
            ans += n%2
            #n = n // 10 # shift right i.e discard last bit|number
            n >>= 1
        return ans

    def _app3(n):
        '''via string cnt'''
        return sum(1 for i in bin(n)[2:] if int(i))

    return _app1(n)

def reverse_a_bit(n: int):
    ''' 1001 '''
    def reverseBits1(n: int) -> int:
        res = 0
        # 1 calculate from RHS evry bit
        for i in range(32):
            bit = (n >> i) & 1 # shift number by
            res = res | (bit << (31-i))  # place calculated bit at LHS
        return res

    def reverseBits2(n: int) -> int:
        #num = int(bin(n)[2:].zfill(0)[::-1], 2)
        num = int(f'{n:032b}'[::-1], 2)
        return num

    return reverseBits1(n)