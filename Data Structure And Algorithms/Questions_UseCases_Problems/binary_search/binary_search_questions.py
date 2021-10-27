from typing import List


# 1
def order_agnostic_binary_search(arr, target, nonDecreasing=None, start=0, end=-1):
    ''' Order Agnostic Binary Search '''
    if not arr:
        raise Exception("array is empty")
    if end == -1:
        end = len(arr) - 1
    if arr[0] == arr[-1]:
        # All elements in {arr} are same
        return 0 if arr[0] == target else -1

    if not nonDecreasing:
        nonDecreasing = arr[0] < arr[-1]

    # if arr[0] < arr[-1]:
    if nonDecreasing:
        # {arr} is in non-decreasing Order
        while start <= end:
            mid = start + ((end - start) // 2)
            if target > arr[mid]:
                # Search in Right Part
                start = mid + 1
            elif target < arr[mid]:
                # Search in Left Part
                end = mid - 1
            else:
                return mid
    else:
        # {arr} is in non-increasing Order
        while start <= end:
            mid = start + ((end - start) // 2)
            if target > arr[mid]:
                # Search in Left Part
                end = mid - 1
            elif target < arr[mid]:
                # Search in Right Part
                start = mid + 1
            else:
                return mid
    return -1


# 2
def binary_search_rec(arr, t, s, e):
    ''' BS using recurssive approach'''
    if s > e:
        return -1
    mid = (s + e) // 2
    if arr[mid] == t:
        return mid
    if t < mid:
        return binary_search_rec(arr, t, s, mid - 1)
    else:
        return binary_search_rec(arr, t, mid + 1, e)


# 3
def binary_search_plain(arr, target, start=0, end=-1):
    ''' Binary Search for Sorted Array using Iterator Approach '''
    end = end if end != -1 else len(arr) - 1
    while start <= end:
        mid = start + ((end - start) // 2)
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return mid
    return -1


# 4
def ceil(arr, target):
    '''
    find the position of element that is first-most >= target using BS
    '''
    if target > arr[-1]:
        return -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + ((end - start) // 2)
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return mid
    return start


# 5
def floor(arr, target):
    '''
    find the position of element that is first-most <= target using BS
    '''
    if target < arr[0]:
        return -1
    start, end = 0, len(arr)
    while start <= end:
        mid = start + ((end - start) // 2)
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return mid
    return end

def isqrt(n):
    '''
    math.isqrt() via Binary Search Floor

    Logic ->

    Let's consider
    number - n, divisor - d

    if d divides n into exact d parts then we can say that d is exact square root of n
    if d divides n into more than d parts so -> need to lower the divider
    if d divides n into less than d parts sp -> need to increase the divider
    '''
    s, e = 1, n
    while s <= e:
        m = s + (e-s) // 2
        q = n // m
        if m == q:
            # m divides n into exact m parts, i.e found exact square root
            return m
        elif q > m:
            # m divides n into more than m parts, i.e more parts than expected so increase the divider
            s = m+1
        else:
            # m divides n into less than m parts i.e less parts than expected so decrease the divider
            e = m-1
    return e

# 6
def near(arr, target):
    '''
    find the position of element that is near to target using BS
    '''
    if target > arr[-1]:
        return len(arr) - 1
    elif target < arr[0]:
        return 0
    start, end = 0, len(arr)
    while start <= end:
        mid = start + ((end - start) // 2)
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return mid
    return end if abs(arr[start] - target) > abs(arr[end] - target) else start

# 7
def start_and_end(arr, target):
    '''
    Get the leftmost & rightmost index of target in arr
    '''
    def bs(arr, target, leftMost=True):
        '''
        Assuming array is non-decreasing order
        find the position of element that is
          start = first-most <= target
          end = last-most >= target
        '''
        start, end = 0, len(arr) - 1
        ans = -1
        while start <= end:
            mid = start + ((end - start) // 2)
            if target > arr[mid]:
                start = mid + 1
            elif target < arr[mid]:
                end = mid - 1
            else:
                ans = mid
                # LeftMost
                if leftMost:
                    end = mid - 1
                else:
                    start = mid + 1
        return ans

    left = bs(arr, target)
    right = bs(arr, target, leftMost=False) if left != -1 else -1
    return left, right

# ---- Intermediate ----

# 8
def infinite_array_search(arr, target):
    '''
    Search target in an infinite sorted array i.e Length is not available to you
    '''

    def find_chunk(arr, target):
        '''
        Find the chunk of elements from array arr, where target can be seached
        :return (s, e) -> s -> start index of chunk & e -> end index of chunk  // 0 < s < e < Inf
        '''
        start, end = 0, 1  # start with chunk of size = 2 i.e 2 elements
        while target > arr[end]:
            current_chunk_size = end - start + 1
            # expand chunk exponentially in base 2 - Worst Case is Log(N, 2)
            new_chunk_size = current_chunk_size * 2
            start, end = end + 1, end + new_chunk_size
        return start, end

    s, e = find_chunk(arr, target)
    return binary_search_plain(arr, target, s, e)


# 9
def find_peak_index_in_mountain(arr: List[int]) -> int:
    '''
    arr -> Increasing then Decreasing after some peak val
        Idea -> binary search with custom condition i.e where
        step-1) find middle idx
        step-2) if mid < mid + 1, search in right
        step-3) else search in left
        at the end start & end will point to max element in array
    '''
    s, e = 0, len(arr) - 1
    while s < e:
        m = s + (e - s) // 2
        if arr[m] > arr[m + 1]:
            # search in left part (i.e m can be a candidate for peak val)
            e = m
        else:
            # search in right part (i.e m+1 can be a candidate for peak val)
            s = m + 1
    return s


# 10
def find_peak_element_in_mountain(nums: List[int]) -> int:
    idx = find_peak_index_in_mountain(nums)
    return nums[idx]


# 11
def find_element_in_mountain(nums: List[int], target: int):
    '''
    MOUNTAIN ARRAY Property :-
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
    :param nums: mountain array
    :param target: to be searched
    :return: index
    '''
    peak_idx = find_peak_index_in_mountain(nums)
    if nums[peak_idx] == target:
        return peak_idx
    idx = -1
    if peak_idx != -1:
        # NOTE :- Here assume that there is only 1 Peak in Mountain Array
        # Search in Left Part i.e non-decreasing part
        idx = order_agnostic_binary_search(nums, target, nonDecreasing=True, start=0, end=peak_idx - 1)
        if idx == -1:
            # Search in Right part i.e non-increasing part
            idx = order_agnostic_binary_search(nums, target, nonDecreasing=False, start=peak_idx + 1, end=len(arr) - 1)
    return idx

# ---- Advance ----

# 12
def find_pivot_in_rotated_sorted_array(nums: List[int]) -> int:
    '''
    Find the index of maximum number if array is rotated atleast
    NOTE - pivot is largest elem because there can be only chance that
           largest elem,the following element will always be smallest
    (Assuming Unique elements in array)
    :param nums: list of rotated sorted array
    :return: index of maximum number if array is rotated (i.e except first & last element index)
    '''
    s, e = 0, len(nums) - 1
    while s <= e:
        m = s + (e - s) // 2
        if m < e and nums[m] > nums[m + 1]:
            return m  # pivot found i.e Peak -> smallest
        elif m > s and nums[m - 1] > nums[m]:
            return m - 1  # pivot found i.e Peak -> smallest
        elif nums[s] < nums[m]:
            # increasing left part so max element will lie in right part
            s = m + 1
        else:
            # nums[s] > nums[m]
            # peak can be in left part (as all elem in right part is smaller than left part)
            e = m - 1
    return -1


# 13
def find_pivot_in_rotated_sorted_array_with_duplicates(nums: List[int]) -> int:
    '''
    Find the index of maximum number if array is rotated atleast
    NOTE - pivot is largest elem because there can be only chance that
           largest elem,the following element will always be smallest
    (Array may include duplicate elements in array)
    :param nums: list of rotated sorted array
    :return: index of maximum number if array is rotated (i.e except first & last element index)

    1) num[s] == nums[m] == nums[e]
        in which case we will ignore s & e items after pivot check
    2) When num[s] == nums[m]
       - It delineats that s -> m all elements are same so search in right (after considering first point)
    '''

    s, e = 0, len(nums) - 1
    while s <= e:
        m = s + (e - s) // 2
        if m < e and nums[m] > nums[m + 1]:
            return m  # pivot found i.e Peak -> smallest
        elif m > s and nums[m - 1] > nums[m]:
            return m - 1  # pivot found i.e Peak -> smallest
        elif nums[s] == nums[m] == nums[e]:
            # check and ignore start
            if s < e and nums[s] > nums[s + 1]:
                return s
            else:
                s += 1
            # check and ignore end
            if e > s and nums[e - 1] > nums[e]:
                return e - 1
            else:
                e -= 1
        elif nums[s] <= nums[m]:
            # increasing left part so max element will lie in right part
            # (here if s == m then also it means that s->m all are equal elements)
            s = m + 1
        else:
            # nums[s] > nums[m]
            # peak can be in left part (as all elem in right part is smaller than left part)
            e = m - 1
    return -1


# 14
def search_in_rotated_sorted_array(nums: List[int], target: int, unique=False) -> int:
    if unique:
        kingMaker = find_pivot_in_rotated_sorted_array(nums)
    else:
        kingMaker = find_pivot_in_rotated_sorted_array_with_duplicates(nums)
    # if kingMaker is found i.e we have found 2 asc sorted array
    if kingMaker == -1:
        # No rotation on nums
        binary_search_plain(nums, target)
    elif nums[kingMaker] == target:
        return kingMaker
    elif target < nums[0]:
        # search in right part of kingmaker (i.e lower values bunch)
        binary_search_plain(nums, target, kingMaker + 1)
    else:
        # search in left part of kingmaker (i.e higher values bunch)
        binary_search_plain(nums, target, 0, kingMaker)


# 15
def find_rotation_count_in_sorted_array(nums: List[int], unique=False) -> int:
    if unique:
        pivot_idx = find_pivot_in_rotated_sorted_array(nums)
    else:
        pivot_idx = find_pivot_in_rotated_sorted_array_with_duplicates(nums)
    return pivot_idx + 1




if __name__ == '__main__':
    arr = [1, 2, 5, 14, 16, 19, 23]
    print(floor(arr, 18), ceil(arr, 18), near(arr, 33))

    arr = [1, 2, 5, 14, 14, 16, 16, 16, 19, 23, 23]
    print(start_and_end(arr, 16))
