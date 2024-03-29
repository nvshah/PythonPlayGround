import math

def round_half_up(n, decimals):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier


def round_half_away_from_zero(n, decimals=0):
    rounded_abs = round_half_up(abs(n), decimals)
    return math.copysign(rounded_abs, n)

def clamp(i, l, u):
    return max(l, min(i, u))

def filterOddNums(lst):
    *a, = filter(partial(and_, 1), lst)
    return a

if __name__ == '__main__':
    print(clamp(4, 5, 10))
