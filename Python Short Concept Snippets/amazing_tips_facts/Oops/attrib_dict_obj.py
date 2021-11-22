'''
ReMEMBER :- If attrib not found in current class it will look in super class
'''


class A:
    c = 10  # class variable

    def __init__(self):
        self.x = 20  # instance variable

a = A()

print(a.__dict__)
print(A.__dict__)


print('looked inside instance dict & found x attrib', a.x)
# c is not present inside the a's dictionary so it looks for parent context
print('look to parent ie class A for attrib c', a.c)


