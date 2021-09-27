class Any:
    # Any object can have only 2 attributes i.e x & y
    __slots__ = ('x', 'y')
    #x = 10

a = Any()

#print(a.__dict__)  # Gives error that a does not have __dict__
#print(a.x)  # error still now attributes are not attached
# print(Any.__dict__)

print(Any.__dict__) # valid on class type


'''
Monkey Patching With Constraints via __slots__ 
'''
a.x = 10
a.y = 20

a.z = 30  # Error 'Any' object has no attribute 'z'