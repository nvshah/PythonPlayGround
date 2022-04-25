
def i_square_root_bs(n):
    '''
    return integer val of square root
    :param n: number whose isquare root needs to be the found
    :return: isqrt ans ie int
    '''
    s, e = 0, n
    while s <= e:
        m = s + (e-s) // 2
        if m * m == n:
            return m
        if m * m > n:
            e = m-1
        else:
            s = m+1
    return e  # end will point to floor() or int() of sqrt answer

def square_root_bs(n, p):
    '''
    Approximate square root of n
    :param n: number whose square root needs to be the approximated
    :param p: precision of decimal place
    :return: approximated ans ie float
    '''
    s, e = 0, n
    while s <= e:
        m = s + (e-s) // 2
        if m * m == n:
            return m
        if m * m > n:
            e = m-1
        else:
            s = m+1
    root = e # end will point to floor() or int() of sqrt answer
    #root = i_square_root_bs(n)  # end will point to floor() or int() of sqrt answer
    # print('integer sqrt ', root)
    decimal_step = 0.1
    for _ in range(p):
        while root * root < n:  # try to find the best optimal decimal at each precision level
            root += decimal_step
        root -= decimal_step
        decimal_step = decimal_step/10  # next precision level

    return root

def square_root_newton(n, e):
    '''
    Find square root using Newton Raphson Method
    :param n: number whose square root need to be found
    :param e: error allowed
    :return: square root (n)
    '''
    x = n/2  # take arbitary number guess initially
    while True:
        root = 0.5 * (x + n/x)
        err = abs(root-x)
        if err <= e:
            return root
        x = root

#seive_of_erantosthesis(40)

a = square_root_bs(40, 2)
b = square_root_newton(40, 0.1)
print(a)
print(b)
