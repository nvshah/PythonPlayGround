def bubble_sort(arr):
    '''
    Inplace - Stable Sort
    Sinking Sort, Exchange Sort
    '''
    l = len(arr)
    for i in range(l-1):  # i is counter -> counts l-1 times atmost
        swap_happen = False
        for j in range(1, l):  # j is traverser
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]  # Swap
                swap_happen = True
        if not swap_happen:  # array is sorted if not a single swap happen
            break

if __name__ == '__main__':
    a = [1,5,10,4,2,8]
    a = [10,20,90,88]
    bubble_sort(a)
    print(a)

