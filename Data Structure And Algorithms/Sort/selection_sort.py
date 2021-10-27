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

if __name__ == '__main__':
    a = [1,5,10,4,2,8]
    #a = [10,20,90,88]
    selection_sort(a)
    print(a)

