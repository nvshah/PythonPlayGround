'''
Selection Sort :- select for current position & move on
'''


def selection_sort(arr):
    '''
    Inplace - Not Stable Sort
    Idea :- place element at each pos correctly from L->H
    useful for small size lists
    '''
    l = len(arr)
    for pos in range(l-1, 0, -1):  # pos from rhs -> lhs
        max_idx = max(range(pos+1), key=arr.__getitem__) # get max element index/location
        arr[max_idx], arr[pos] = arr[pos], arr[max_idx]  # swap max element to pos

def selection_sort_rec(arr):
    ''' Idea :- select correct element for current position '''
    size = len(arr)

    def helper(pos):
        if pos == size:  # array is sorted
            return
        min_idx = min(range(pos, size), key=arr.__getitem__) # get min element index/location
        arr[pos], arr[min_idx] = arr[min_idx], arr[pos] # put element at correct location
        helper(pos+1)

    helper(0)


if __name__ == '__main__':
    a = [1,5,10,4,2,8]
    #a = [10,20,90,88]
    selection_sort(a)

    b = [1, 5, 10, 4, 8, 2]
    selection_sort_rec(b)
    print(b)
    print(a)

