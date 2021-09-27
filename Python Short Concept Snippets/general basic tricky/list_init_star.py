class A:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return str(self.a)


if __name__ == '__main__':
    # NOTE -> `*` will copy object references & not create new object
    l = [A(10)] * 5
    print([f'{i}' for i in l])
    l[0].a = 20
    print([f'{i}' for i in l])

    print(isinstance(A(10), A))
    print(type(A(10)))
