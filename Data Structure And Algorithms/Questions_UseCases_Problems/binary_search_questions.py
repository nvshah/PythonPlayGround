from typing import List


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


def binary_search_plain(arr, target, start=0, end=-1):
    ''' Binary Search for Sorted Array using Iterator Approach '''
    end == end if end != -1 else len(arr) - 1
    while start <= end:
        mid = start + ((end - start) // 2)
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def floor(arr, target):
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


def ceil(arr, target):
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


def start_and_end(arr, target):
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


def find_peak_element_in_mountain(nums: List[int]) -> int:
    idx = find_peak_index_in_mountain(nums)
    return nums[idx]


def find_element_in_mountain(nums: List[int], target: int):
    peak_idx = find_peak_index_in_mountain(nums)
    if nums[peak_idx] == target:
        return peak_idx
    idx = -1
    if peak_idx != -1:
        # Search in Left Part i.e non-decreasing part
        idx = order_agnostic_binary_search(nums, target, nonDecreasing=True, start=0, end=peak_idx - 1)
        if idx == -1:
            # Search in Right part i.e non-increasing part
            idx = order_agnostic_binary_search(nums, target, nonDecreasing=False, start=peak_idx + 1, end=len(arr) - 1)
    return idx


if __name__ == '__main__':
    arr = [1, 2, 5, 14, 16, 19, 23]
    print(floor(arr, 18), ceil(arr, 18), near(arr, 33))

    arr = [1, 2, 5, 14, 14, 16, 16, 16, 19, 23, 23]
    print(start_and_end(arr, 16))
