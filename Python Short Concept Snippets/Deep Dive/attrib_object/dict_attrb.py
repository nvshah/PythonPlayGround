class Car:
    def __init__(self, name):
        self.brand = name

    def start(self):
        self.speed = 10

c = Car(name='Toyota')

print(c.__dict__)  # {'brand': 'Toyota'}
c.start()
# An eg of monkey patching
print(c.__dict__) # {'brand': 'Toyota', 'speed': 10}
print(Car.__dict__)