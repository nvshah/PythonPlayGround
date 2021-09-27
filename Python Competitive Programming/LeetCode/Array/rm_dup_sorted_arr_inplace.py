from typing import List


def removeDuplicates(nums: List[int]) -> int:
	'''
	:param nums: list of numbers
	:return: total number of non duplicates
	Idea -> track 2 seekers i.e start & lead that will finalize starting pos 1 by 1
	'''
	l = len(nums)
	if l < 1:
		return l
	start = 0  # Current Position of unique index from start
	lead = 1   # traversal one time seeker

	while lead < l:
		while nums[start] == nums[lead]:
			lead += 1
			if lead == l:
				break
		else:
			start += 1
			nums[start], nums[lead] = nums[lead], nums[start]
			lead += 1

	return start + 1


if __name__ == '__main__':
	# Test Cases Run Successfully
	nums = [1, 1, 2]
	nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
	nums = [1,2]
	nums = [1,1]
	left = removeDuplicates(nums)
	print(left)
	print(nums)
