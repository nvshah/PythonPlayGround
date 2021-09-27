# rBy -> rotate by
def leftRotate(arr, rBy):
    len_arr = len(arr)
    n_rby = rBy % len_arr if rBy > len_arr else rBy
    return [*arr[n_rby:], *arr[:n_rby]]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

ra = leftRotate(a, 19)

print(ra)
