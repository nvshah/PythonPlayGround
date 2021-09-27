# two_sumpy

import itertools as it
from typing import List


# Approach 1 Deprecated, (As this works only for Positive integers)
def twoSum_a1(nums: List[int], target: int) -> List[int]:
	f_nums = (ne for ne in enumerate(nums) if ne[1] <= target)
	pairs = it.combinations(f_nums, 2)
	for ne1, ne2 in pairs:
		if ne1[1] + ne2[1] == target:
			return [ne1[0], ne2[0]]


def isOdd(num):
	return bool(num % 2)


''' (Deprecated) Approach2
(When nums may contains negatvie numbers)
Idea -> seperate odds & even nums &
		odd = even + odd
		even = odd + odd | even + even
'''
def twoSum_a2(nums: List[int], target: int) -> List[int]:
	# Traditional Approach as mentioned in Idea
	odds = []
	evens = []
	# In-case when all numbers in list are positive (no chance of subtraction)
	temp = []
	useless = False

	total_comp = 0

	for i in range(len(nums)):
		if isOdd(nums[i]):
			odds.append(i)
		else:
			evens.append(i)
		if (not useless) and (nums[i] >= 0):
			if nums[i] <= target:
				temp.append(i)
		else:
			useless = True

	if not useless:
		# All numbers in nums are positive so Target can't be result of subtraction
		pairs = it.combinations(temp, 2)
	elif isOdd(target):
		# Target is Odd Number
		pairs = it.product(odds, evens)
	else:
		# Target is Even Number
		pairs = it.chain(it.combinations(odds, 2), it.combinations(evens, 2))

	for i1, i2 in pairs:
		if nums[i1] + nums[i2] == target:
			print('Total Comparisions : ', total_comp)
			return [i1, i2]
		total_comp += 1


'''
Idea -> seperate odds & even nums &
odd = even + odd
even = odd + odd | even + even
'''
def twoSum(nums: List[int], target: int) -> List[int]:
	odds = []
	evens = []

	for i in range(len(nums)):
		if isOdd(nums[i]):
			odds.append(i)
		else:
			evens.append(i)

	if isOdd(target):
		# Odd Number
		pairs = it.product(odds, evens)
	else:
		# Even Number
		pairs = it.chain(it.combinations(odds, 2), it.combinations(evens, 2))

	for i1, i2 in pairs:
		if nums[i1] + nums[i2] == target:
			return [i1, i2]


if __name__ == '__main__':
	ans = twoSum([2, 7, 11, 15], 9)
	print(ans)

	ans = twoSum([3, 2, 4], 6)
	print(ans)

	ans = twoSum([3, 3], 6)
	print(ans)

	ans = twoSum([-3, 4, 3, 9], 0)
	print(ans)
