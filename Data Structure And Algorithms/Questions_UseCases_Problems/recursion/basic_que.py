from math import log10

def revers_num(n):
    sum = 0
    def _app1(n):
        ''' Via String Way '''
        if n % 10 == n:
            return n
        q, r = divmod(n, 10)
        return int(f'{r}{_app1(q)}')

    def _app2(n):
        ''' As We do digit by digit & sum variable '''
        nonlocal sum
        if n == 0:
            return
        q, r = divmod(n, 10)
        sum = sum * 10 + r
        _app2(q)

    def _app3(n):
        '''
          via size of n & a helper function for doing recursive task
        '''
        def _helper(n, size):
            if n == 0:
                return 0
            q, r = divmod(n, 10)
            return r*pow(10, size-1) + _helper(q, size-1)
        digits = 1 if n == 0 else int(log10(n)) + 1
        return _helper(n, digits)

    return _app3(n)



if __name__ == '__main__':
    print(revers_num(1032))