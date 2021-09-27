def f():
    print('HAhA')

e = compile('from __main__ import f as f2', filename='sample', mode='exec')
exec(e)
f2()