nums = [3, 5, 2, 1, 4]
letters = ['c', 'r', 'b', 'a', 'e']

data = sorted(zip(nums, letters))

nums_n, letters_n = zip(*data)
print(nums_n)
print(letters_n)

# - TURN 2 seperate list into dictionary

# - zip() & enumerate()

a = [1,2,3,4]
b = [10,20,30,40]

for i, *x in enumerate(zip(a, b)):
    print(f'index : {i} -> {x}')

for i, (x, y) in enumerate(zip(a, b)):
    print(f'index : {i} -> {x} : {y}')