def gen():
    for i in range(5):
        print(f'Yielding {i}', end='<->')
        yield i

#1.
*l, = gen()   # Here entire gen() is iterated on assignment only before using the l
print(l)  #list


#2.
l2 = [1,2,3]
l2[1:1] = gen() # Here also entire gen() is iterated on assignment only
'''
=> So we can see that with starred assignment & unpacking do greedy operation on generator/iterator
=> slice assignment also behaves eagerly with the generator & fetch all elements at once greedily
'''


#3...
def f(a1,*a2):
    print(a1, a2)
    l,*_ = a2
    print(*l)  # 1 2 3

f(1,(i for i in [1,2,3]))








