def insertion_sort(arr):
    '''
    Inplace - Stable Sort
    useful for inserting new element into sorted list
    or when array is partially sorted
    '''
    l = len(arr)
    for i in range(l-1):  # i is counter -> counts l-1 times always
        j = i+1  # virtually new element added at the end of list for now
        while j > 0 and arr[j] < arr[j-1]:  # detect location of new element in already sorted array
            arr[j-1], arr[j] = arr[j], arr[j-1]  # swap
            j -= 1



if __name__ == '__main__':
    a = [1,5,10,4,2,8]
    #a = [10,20,90,88]
    a = [0, -23, 430, 2, 10]
    insertion_sort(a)
    print(a)

