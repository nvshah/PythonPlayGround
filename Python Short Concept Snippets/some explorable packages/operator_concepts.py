import operator

f1 = operator.itemgetter(3)
t1 = f1((1,2,3,4,4))
print(t1) # 4

f2 = operator.itemgetter(2,3,5)
t1 = f2((1,2,3,4,6,7,8))
print(t1) # (3,4,7)


# sorted and attrgetter

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name} - {self.age}'


e1 = Employee('Manan', 25)
e2 = Employee('Rupali', 22)
e3 = Employee('Vishwa', 23)

le = [e1, e2, e3]

s_le = sorted(le, key=operator.attrgetter('age'))
print(s_le)  # [Rupali - 22, Vishwa - 23, Manan - 25]