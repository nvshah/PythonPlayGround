from collections import namedtuple

Car = namedtuple("Car", 'color average')

my_car = Car('red', 100)

print(my_car.color, my_car.average)