from functools import partial

def f1(a, b, /, c='3rd', d='4th'):
    print(a, b, c, d)

f2 = partial(f1, 'first', c='third')

f2('2nd') # first fourth third 4th

f2('2nd', d='4th')