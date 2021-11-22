'''
 Divide & conquer Technique
 Time :- O(n*lg(n))
'''


def merge_sort(arr):
    '''
     implement merge sort uing extra array (not in-place)
    '''

    def merge(a1, a2):
        ''' merge 2 sorted arrays a1 & a2 '''
        i = j = k = 0
        size1, size2 = len(a1), len(a2)
        res = [0]*(size1 + size2)

        while i < size1 and j < size2:
            if a1[i] <= a2[j]:
                res[k] = a1[i]
                i += 1
            else:
                res[k] = a2[j]
                j += 1
            k += 1

        # there may be chances that elements are left in either a1 or a2
        while i < size1:
            res[k], i, k = a1[i], i+1, k+1

        while j < size2:
            res[k], j, k = a2[j], j+1, k+1

        return res

    def sort(arr):
        ''' divide & merge '''
        size = len(arr)
        if size == 1:  # cannot divide further
            return arr

        mid = size // 2
        # Divide
        left = sort(arr[:mid]) # sort left
        right = sort(arr[mid:]) # sort right part
        # Merge
        return merge(left, right) # merge sorted left & right part

    return sort(arr)

def merge_sort_i(arr):
    ''' merge sort inplace '''

    def merge(s, m, e):
        '''
        :param s : start
        :param m : middle
        :param e : end inclusive
        '''
        res = [0]*(e-s)
        p1, p2, k = s, m, 0
        while p1 < m and p2 < e:
            if arr[p1] > arr[p2]:
                res[k] = arr[p2]
                p2 += 1
            else:
                res[k] = arr[p1]
                p1 += 1
            k += 1
        while p1 < m:
            res[k], p1, k = arr[p1], p1+1, k+1
        while p2 < e:
            res[k], p2, k = arr[p2], p2+1, k+1

        arr[s:e] = res   # modify inplace

    def merge2(s, m, e):
        ''' Takes less auxilary space ie second-half as extra space not total elem as extra space '''
        second_l = e-m
        extra = [0] * second_l
        i, j, k, l = m-1, e-1, -1, m-1

        while i >= s and j >= m:
            if k >= -second_l:
                if arr[i] > arr[j]:
                    extra[k] = arr[i]
                    i -= 1
                else:
                    extra[k] = arr[j]
                    j -= 1
                k -= 1
            else:
                if arr[i] > arr[j]:
                    arr[l] = arr[i]
                    i -= 1
                else:
                    arr[l] = arr[j]
                    j -= 1
                l -= 1

        while j >= m:
            if k >= -second_l:
                extra[k], k, j = arr[j], k-1, j-1
            else:
                arr[l], j, l = arr[j], j-1, l-1

        arr[m:e] = extra  # less extra space than whole one


    def sort(s, e):
        print('sort', s, e)
        '''
        :param s : start index of arr
        :param e : end index of arr
        '''
        if e - s <= 1:  # 1 element left
            return
        #m = ceil((s+e) / 2)
        m = (s+e) // 2
        sort(s, m)  # sort left
        sort(m, e)  # sort right
        merge(s, m, e)  # merge left + right
        #merge2(s, m, e)

    sort(0, len(arr))


if __name__ == '__main__':
    a = [2, 5, 1, 10, 6, 3]
    a = [2, 1, 4]
    b = merge_sort(a)
    print(b)
    merge_sort_i(a)
    print(a)



