def is_arr_sorted(lst):
    ''' check whether arr is sorted or not using recursion'''
    def helper(arr, l, r):
        '''via 2 pointer '''
        if l >= r: # all elements are visited
            return True
        # check from both end if array is sorted
        return arr[l] < arr[l+1] and arr[r-1] < arr[r] and helper(arr, l+1, r-1)

    def helper2(arr, p):
        ''' via 1 pointer'''
        if p == len(arr)-1: # all elements are visited
            return True
        # check from both end if array is sorted
        return arr[p] < arr[p+1] and helper(arr, p+1)

    #return helper2(lst, 0)
    return helper(lst, 0, len(lst)-1)

def linear_search(lst, target):
    size = len(lst)

    def helper_contains(arr, idx):
        '''check if element exists in arr '''
        if idx == size:
            return False
        return arr[idx] == target or helper_contains(arr, idx+1)

    def helper_index(arr, idx):
        ''' find idx of elemennt in arr'''
        if idx == size:
            return -1
        return idx if arr[idx] == target else helper_index(arr, idx+1)

    def helper_last_index(arr, idx):
        ''' find idx of element in arr from right side'''
        if idx == -1:
            return -1
        return idx if arr[idx] == target else helper_last_index(arr, idx-1)

    def helper_find_all_index(arr, idx, result=[]):
        '''find all the idx of element in arr'''
        if idx == len(arr):
            return result
        if arr[idx] == target:
            result.append(idx)
        return helper_find_all_index(arr, idx+1)

    def helper_find_all_index_a2(arr, idx):
        ''' find all the idx w.o taking list as a pram '''
        l = []
        if idx == len(arr):
            return []
        if arr[idx] == target:
            l.append(idx)
        # get list of any elements if present ahead as well
        find_rest_idx = helper_find_all_index(arr, idx+1)
        l.extend(find_rest_idx)
        return l

    #return helper_index(lst, 0)
    return  {
        'presence ' : helper_contains(lst, 0),
        'leftmost index ': helper_index(lst, 0),
        'rightmost index ': helper_last_index(lst, len(lst)-1),
        'all index': helper_find_all_index(lst, 0)
    }


def rotated_sorted_arr(arr, target):
    def _helper(s, e):
        if s > e:
            return -1
        m = (s + e) // 2
        if arr[m] == target:
            return m
        if arr[s] <= arr[m]:
            if arr[s] <= target <= arr[m]:  # first half is sorted
                return _helper(s, m-1)
            else:
                return _helper(m+1, e)
        else:
            if arr[m] <= target <= arr[e]:  # 2nd half is sorted
                return _helper(m+1, e)
            else:
                return _helper(s, m-1)
    return _helper(0, len(arr)-1)




if __name__ == '__main__':
    l = [1, 4, 2, 9, 5, 10, 5, 10, 5]
    print(linear_search(l, 5))

    l2 = [5,6,7,8,9,1,2,3,4]
    print(rotated_sorted_arr(l2, 2))
