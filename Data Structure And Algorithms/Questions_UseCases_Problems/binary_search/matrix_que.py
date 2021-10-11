from math import ceil
from typing import List, Tuple

def binary_search(arr, t):
    s, e = 0, len(arr)-1
    while s <= e:
        m = s + (e - s) // 2
        if arr[m] == t:
            return m
        elif t > arr[m]:
            s = m+1
        else:
            e = m-1
    return -1

def search_in_matrix_1(matrix: List[List[int]], target: int)->Tuple[int, int]:
    '''
    :param matrix: matrix where row & col are sorted
    :param target: to be search in matrix
    :return: (r, c)
    '''
    assert len(matrix) != 0, "Matrix can't be empty"
    l = len(matrix)
    r, c = l, l - 1
    while r < l and c >= 0:
        if matrix[r][c] == target:
            return (r, c)
        elif target > matrix[r][c]:
            # Ignore current row
            r += 1
        else:
            # Ignore current col
            c -= 1
    return (-1, -1)


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    '''
    :param matrix: matrix where row is sorted & forst element of each row is > than last element of prev row
    :param target: to be search in matrix
    :return: (r, c)
    '''
    r_s, r_e = 0, len(matrix)-1
    while r_s != r_e:
        m = ceil((r_s + r_e) / 2) # giving priority to rhs idx
        num = matrix[m][0]
        if num == target:
            return (m, 0)
        elif target > num:
            r_s = m  # target can be in middle row so r_s -> m
        else:
            r_e = m-1  # target will always beyond middle row at moment
    idx = binary_search(matrix[r_s], target)
    return (r_s, idx) if idx != -1 else (-1, -1)

if __name__ == '__main__':
    matrix = [[-8, -7, -5, -3, -3, -1, 1],
              [2, 2, 2, 3, 3, 5, 7],
              [8, 9, 11, 11, 13, 15, 17],
              [18, 18, 18, 20, 20, 20, 21],
              [23, 24, 26, 26, 26, 27, 27],
              [28, 29, 29, 30, 32, 32, 34]]
    target = 3

    i = searchMatrix(matrix, target)
    print(i)