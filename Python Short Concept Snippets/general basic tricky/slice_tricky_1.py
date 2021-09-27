print([1,2,3,4,5][-1:-0:-1]) # 5,4,3,2,1

# using slice() ------------------------------------

last_three = slice(-3, None)
first_three = slice(3)
every_other = slice(0, None, 2)

l = range(10)
print(l[last_three])  # range(7, 10)
print(l[first_three])  # range(0, 3)
print(l[every_other])  # range(0, 10, 2)
