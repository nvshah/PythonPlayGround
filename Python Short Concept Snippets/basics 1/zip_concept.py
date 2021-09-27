nums = [3, 5, 2, 1, 4]
letters = ['c', 'r', 'b', 'a', 'e']

data = sorted(zip(nums, letters))

nums_n, letters_n = zip(*data)
print(nums_n)
print(letters_n)

# - TURN 2 sepeerate list into dictionary