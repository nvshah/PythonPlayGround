class Cat:
    pass

c = Cat()
c.name = "Tom"  # Monkey-Patching

# Attribute to object attached, here only
print(c.__dict__) #{'name': 'Tom'}

