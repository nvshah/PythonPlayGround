from typing import List


def removeElement(nums: List[int], val: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        if start == end:
            if val == nums[end]:
                end -= 1
            break
        while nums[end] == val:
            # cnt += 1
            end -= 1
            if end == start:
                if val == nums[end]:
                    end -= 1
                break
        else:
            while nums[start] != val:
                start += 1
                if start == end:
                    break
                # cnt += 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

    return end + 1

def removeElement_2(nums: List[int], val: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        if end == start:
            if nums[end] == val:
                return end
            return end + 1
        while nums[end] == val:
            # cnt += 1
            end -= 1
            if end == start:
                if nums[end] == val:
                    return end
                return end + 1
        while nums[start] != val:
            start += 1
            if start == end:
                return end + 1
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

    return end + 1

arr = [3, 2, 2, 3]
val = 3
arr = [0,1,2,2,3,0,4,2]
val = 2
arr = [1]
val = 1
arr = [3,3]
val = 3
arr = [2,2,3]
val = 2
arr = [4, 5]
val = 4
ans = removeElement(arr, val)
print(ans)
print(arr)
