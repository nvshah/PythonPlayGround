
# task :- create UpperCase for Tuple

'''
Note ; You can also makes proxy obj that do upper() & forward its call to underlying
       tuple
       this will impact performance
       wrapper being written in python will take significant time



'''

class UpperCaseTuple(tuple):

    def __new__(cls, iterable):
        g = (a.upper() for a in iterable)
        print(id(g))
        return super().__new__(cls, g)

    #def __init__(self, iterable):
        # We cannot do this as tuple is immutable so we need to
        # do this before object is created ie __new__
        # for i, arg in enumerate(iterable):
        #     self[i] = arg.upper()

    def __init__(self, iterable):
        print(id(self))


class UpperCaseList(list):
    def __init__(self, iterable):
        print(super())
        super().__init__(iterable)
        for i, arg in enumerate(iterable):
            self[i] = arg.upper()

if __name__ == '__main__':
    l = ['a', 'b', 'c']
    #o1 = UpperCaseList(l)
    #print(o1)

    o2 = UpperCaseTuple(l)
    print(id(o2))