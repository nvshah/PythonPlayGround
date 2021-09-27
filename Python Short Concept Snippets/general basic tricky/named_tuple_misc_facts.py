from collections import namedtuple

Person = namedtuple('Person', ('name', 'age'))
Pet = namedtuple('Pet', ('name', 'age'))

naruto = Person('Naruto', 20)
fox = Pet('Naruto', 20)

# Here though naruto & fox are diff instance in memory
# bizarre though name of both tuple are diff it's same
print(naruto == fox, naruto is fox)  # True False

# Normal Tuple way  ------------------

t1 = ('Naruto', 20)
t2 = ('Naruto', 20)
print(t1 is t2, t1 == t2)  # True True