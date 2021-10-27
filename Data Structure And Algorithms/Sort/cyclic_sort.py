def cyclic_sort(arr):
    '''
    Inplace - Uniqye element & 1 -> n  Continuous values
    property :- index = element_at_index - 1
    '''
    # l = len(arr)
    # for i in range(l-1):  # i is counter -> counts l-1 times always
    #     # place correct element at index i
    #     while arr[i] != i + 1:  # 1 check till element at current index i is properly placed
    #         correct_idx = arr[i] - 1  # 2. correct idx for current element
    #         arr[i], arr[correct_idx] = arr[correct_idx], arr[i]  # 3. swap

    i, l = 0, len(arr)
    while i < l:
        correct_idx = arr[i] - 1  # correct idx of current element
        if arr[correct_idx] != arr[i]:
            # move element to its correct index
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]  # Swap
        else:
            i += 1

# def cyclic_sort_i2(arr):
#     ''' For given index find its correct element'''
#     i, l = 0, len(arr)
#     while i < l:
#         correct_idx = arr[i] - 1  # correct idx of current element
#         if i != correct_idx: # duplicate element i.e correct idx already had element placed correctly
#             arr[i], arr[correct_idx] = arr[correct_idx], arr[i]  # Swap
#         else:
#             i += 1

# def cyclic_sort_i3(arr):
#     '''for given element Make element move to its correct position '''
#     i, l = 0, len(arr)
#     while i < l:
#         correct_idx = arr[i] - 1  # correct idx of current element
#         if arr[correct_idx] != arr[i]: # duplicate element i.e correct idx already had element placed correctly
#             # move element to its correct index
#             arr[i], arr[correct_idx] = arr[correct_idx], arr[i]  # Swap
#         else:
#             i += 1

if __name__ == '__main__':
    a = [3, 5, 1, 2, 4]
    # sa = [3, 2, 6, 1, 4, 5]
    #a = [5,4,3,2,1]
    cyclic_sort(a)
    print(a)

