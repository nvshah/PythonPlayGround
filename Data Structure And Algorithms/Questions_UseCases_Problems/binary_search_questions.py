def binary_search_plain(arr, target, start, end):
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
    def bs(arr, target, leftMost = True):
        '''
        Assuming array is non-decreasing order
        find the position of element that is
          start = first-most <= target
          end = last-most >= target
        '''
        start, end = 0, len(arr)-1
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

if __name__ == '__main__':
    arr = [1, 2, 5, 14, 16, 19, 23]
    print(floor(arr, 18), ceil(arr, 18), near(arr, 33))

    arr = [1, 2, 5, 14, 14, 16, 16, 16, 19, 23, 23]
    print(start_and_end(arr, 16))
