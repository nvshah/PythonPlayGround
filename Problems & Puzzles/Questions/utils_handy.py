def get_digits(n, func=None):
    '''
    return generator of digits
    if func provided then digit is mapped to that func & then returned
    '''
    while n != 0:
        n, r = divmod(n, 10)
        yield func(r) if func else r