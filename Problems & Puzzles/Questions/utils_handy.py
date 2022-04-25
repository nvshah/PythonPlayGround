from math import log10

def get_digits(n, func=None):
    '''
    return generator of digits
    if func provided then digit is mapped to that func & then returned
    '''
    while n != 0:
        n, r = divmod(n, 10)
        yield func(r) if func else r


def get_digits(n, key, rev=False):
    if rev:  # In reverse manner ie from LSB -> MSB
        while n:
            n, r = divmod(n, 10)
            yield r if not key else key(r)
    else: # from MSB -> LSB
        digits = int(log10(n))
        for i in range(digits):
            d, n = divmod(n, pow(10, digits-1))
            yield d if not key else key(d)