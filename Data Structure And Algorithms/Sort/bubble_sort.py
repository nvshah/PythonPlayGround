def bubble_sort(arr):
    '''
    Inplace - Stable Sort
    Sinking Sort, Exchange Sort
    '''
    l = len(arr)
    for i in range(l-1):  # i is counter -> counts l-1 times atmost
        swap_happen = False
        for j in range(1, l-i):  # j is traverser
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]  # Swap
                swap_happen = True
        if not swap_happen:  # array is sorted if not a single swap happen
            break

def bubble_sort_rec(arr):
    '''
     sort the array using bubble sort recursively (inplace)
    '''
    def helper(c, m, s):
        '''
        :param c: number of comparisions needs to be made
        :param m: comparisions made so far
        :param s: swaapped in this turn c, m
        '''
        if c == 0:  # all turns are over
            return
        if c == m:  # all comparisons are made in this turn
            if s:  # as no swap happens in this round so no required to call further
                helper(c-1, 0, False)
            return
        # m is also considered as ptr pting to idx in array
        if arr[m] > arr[m+1]:
            arr[m], arr[m+1] = arr[m+1], arr[m]  # swap
            s = True # swap happens
        helper(c, m+1, s)  # 1 comparison made in this turn
    size = len(arr)
    helper(size-1, 0, False)  # comparisons needs to be made = size of arr - 1


if __name__ == '__main__':
    a = [1,5,10,4,2,8]
    #a = [10,20,90,88]
    #bubble_sort(a)
    b = [5, 3, 10, 2, 8]
    b = [1, 2, 3, 5, 4]
    bubble_sort_rec(b)
    print(b)

