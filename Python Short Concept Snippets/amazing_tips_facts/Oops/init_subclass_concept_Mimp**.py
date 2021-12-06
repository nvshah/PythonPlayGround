class A:
    _registry = {} # static obj shared by diff subclasses

    # this will be called when subclass is defined
    def __init_subclass__(cls, **kwargs):
        print('inside')
        super().__init_subclass__()
        cls._registry[kwargs['key']] = kwargs['value']


    def getClasses(self):
        print(self._registry)

class B(A, key='B', value='Class B'):
    pass
    # def __init__(self):
    #     print('init in B')

class C(A, key='C', value='Class C'):
    pass
    # def __init__(self):
    #     print('init in C')

b = B()
b.getClasses()

