''':var
vars() gives us dictionary representation of all defined variables in the scope of a defined python script
'''

class Person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        self.speed = 1
        print(vars())   # empty vars() = locals()
        print(locals()) # As here there is only 1 local variable i.e self

p = Person(name='Manoj')

p.walk()
print(vars())  #empty vars() is equi to locals() = here same as globals()


#----------------------------------------------------------

s = "This is {dog_name} and he has {eye_color} eyes"
print(s.format(dog_name = "rudra",eye_color = "black"))

dog_name, eye_color = "rudra",'black'
print(s.format(**vars()))

dog_name, eye_color = "rudra",'black'
print(s.format_map(vars()))