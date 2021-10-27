def n_to_one(n: int):
    '''
    print n to 1 using recursion
    '''
    if n == 0:
        return
    print(n)
    n_to_one(n-1)

def one_to_n(n: int):
    '''
    print n to 1 using recursion
    '''
    if n == 0:
        return
    one_to_n(n-1)
    print(n)

def n_to_one_to_n(n: int):
    '''
    print Mountain with Decr + Incr
    '''
    if n == 0:
        return
    print(n)
    n_to_one_to_n(n-1)
    print(n)

if __name__ == '__main__':
    n_to_one_to_n(3)
