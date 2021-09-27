def binarySearch(arr, target):
    '''
    Binary Search - Basic Implementation i.e Order Agnostic Binary Search
    Assuming arr is sorted
    '''
    if not arr:
        raise Exception("array is empty")
    start, end = 0, len(arr) - 1
    if arr[0] == arr[-1]:
        # All elements in {arr} are same
        return 0 if arr[0] == target else -1
    if arr[0] < arr[-1]:
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


def binarySearch_rec(arr, t, s, e):
    '''
    Binary Search using Recurssive approach
    :param arr - array
    :param t - target
    :param s - start idx
    :param e - end idx
    '''
    if s > e:
        return -1
    mid = (s + e) // 2
    if arr[mid] == t:
        return mid
    if t < mid:
        return binarySearch_rec(arr, t, s, mid - 1)
    else:
        return binarySearch_rec(arr, t, mid + 1, e)


# Deprecated for fromLeft & fromRight As that can go to O(log n) in worst case
# i.e all elements except first & last are target
def binary_search_enhanced(arr, target, fromLeft=False, fromRight=False):
    """
    Binary Search - Enhanced Implementation i.e Order Agnostic Binary Search
    @:param arr - sorted array
    @:param target - to be search in arr
    @:param fromLeft - if multiple target present then priortise the left most
    @:param fromRight - if multiple target present then priortise the Right most
    """
    assert not (fromLeft and fromRight), "Cannot Prioritize LeftMost & RightMost at same time"
    if not arr:
        raise Exception("array is empty")
    start, end = 0, len(arr) - 1
    ans = -1
    if arr[0] == arr[-1]:
        # All elements in {arr} are same
        return 0 if arr[0] == target else -1
    if arr[0] < arr[-1]:
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
                ans = mid
                break
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
                ans = mid
                break
    if ans != -1:
        # prioritse left most index of target
        if fromLeft:
            trav = ans - 1
            while trav >= 0 and arr[trav] == target:
                # traverse left until target is neighbour
                trav -= 1
            ans = 0 if trav == 0 else trav + 1
        # prioritse left most index of target
        elif fromRight:
            trav = ans + 1
            while trav < len(arr) and arr[trav] == target:
                # traverse right until target is neighbour
                trav += 1
            ans = len(arr) - 1 if trav == len(arr) else trav - 1
    return ans


# O(log n) Worst Case - Better Soln
def binary_search_enh(arr, target, fromLeft=False, fromRight=False):
    """
    Binary Search - Enhanced Implementation i.e Order Agnostic Binary Search
    @:param arr - sorted array
    @:param target - to be search in arr
    @:param fromLeft - if multiple target present then priortise the left most
    @:param fromRight - if multiple target present then priortise the Right most
    """
    assert not (fromLeft and fromRight), "Cannot Prioritize LeftMost & RightMost at same time"
    if not arr:
        raise Exception("array is empty")
    start, end = 0, len(arr) - 1
    ans = -1
    if arr[0] == arr[-1]:
        # All elements in {arr} are same
        return 0 if arr[0] == target else -1
    if arr[0] < arr[-1]:
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
                ans = mid
                # Don't stop if we want to find LeftMost or RightMost index
                if fromLeft:
                    end = mid - 1  # Search in Left Half for repeated target
                elif fromRight:
                    start = mid + 1  # Search in Right Half for repeated target
                else:
                    break
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
                ans = mid
                # Don't stop if we want to find LeftMost or RightMost index
                if fromLeft:
                    end = mid - 1  # Search in Left Half for repeated target
                elif fromRight:
                    start = mid + 1  # Search in Right Half for repeated target
                else:
                    break
    return ans


if __name__ == '__main__':
    a = [2, 4, 6, 10, 30, 40, 40, 40, 40, 40, 55, 56, 56, 56, 56]
    idx = binary_search_enh(a, 56, False, True)
    print(idx)

    b = [1,2,3,4,4,10,20]
    idx = binarySearch_rec(b, 10, 0, len(b)-1)
    print(idx)
