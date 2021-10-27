def sum_of_digits(n):
    if n == 0:
        return 0
    q, r = divmod(n, 10)
    return r + sum_of_digits(q)


def prod_of_digits(n):
    if n % 10 == 0:
        return n
    q, r = divmod(n, 10)
    return r * prod_of_digits(q)