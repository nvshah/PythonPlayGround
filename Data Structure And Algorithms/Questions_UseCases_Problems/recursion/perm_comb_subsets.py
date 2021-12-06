from typing import List

'''
SUBSET methods :- take it & ignore it
  
  1) Permutation :- only take it (No ignore)
'''

def subsets(arr):
    '''
    Subset = Non Adjacent element list
    :param arr: array of nums
    :return: array of subsets
    '''
    ans = []

    def helper(processed, unprocessed):
        if not unprocessed:  # nothing left to explore ie leaf node
            ans.append(processed)
            return
            #return processed
        # Take it
        helper(processed + [unprocessed[0]], unprocessed[1:])
        # Reject It
        helper(processed, unprocessed[1:])

        #return [t, r]
    #return helper([], arr)
    helper([], arr)
    return ans

def subsets2(nums: List[int]) -> List[List[int]]:
    '''
        Use Recursion to obtain sublists
        When you encounter the Leaf Node in DT, you will get one of possible sublist
    '''

    res = []
    subset = []  # temp list store the current sublist members
    size = len(nums)

    def dfs(i):
        '''
         i -> pos at where from we need to look for subsets
        '''
        if i == size:    # Reach to the Leaf of DT where you get one of possible subset
            res.append(subset.copy())
            return

            # Take num[i]
        subset.append(nums[i])
        dfs(i+1)

        # Check for subsets possibilities discarding the nums[i]
        subset.pop()
        dfs(i+1)

    dfs(0)
    return res

def permutation_dfs(arr):
    ''' Find Permutation via Explore & BackTrack '''
    t = []  # list that holds current permute
    ans = []  # list of all permutes
    size = len(arr)
    available = [1]*size # to check which element are available currently to create a single permute

    def dfs():
        if len(t) == size:
            ans.append(t.copy())
            return

        for i in range(size):
            if available[i]:
                # EXPLORE -----
                t.append(arr[i])
                available[i] = 0
                dfs()
                # BACKTRACK -----
                available[i] = 1
                t.pop()
    dfs()
    return ans

def permutation_pup(arr):
    '''
    Find permutations without needs of backtracking (only Explore)
    Keep track of processed & unprocessed parts from starting
    so at the end processed part will be one of possible ans when unprocessed part is empty
    '''
    ans = []

    def explore(p, up):
        '''
        explore the permutation of p with up
        IDEA :- Go character by character as level progress
        :param p: processed part
        :param up: unprocessed part
        :return: permutation possible combining processed & unprocessed part
        '''
        if not up:
            ans.append(p)
            return
        print('Level :-', len(p)+1)
        # draw first character from unprocessed at each level
        new_e = up[0]
        # number of slots available (in processed part)
        # so that new_e can be put into processed part
        slots_available = len(p) + 1
        for i in range(slots_available):  # slots to be fill
            new_p = [*p[:i], new_e, *p[i:]]
            # as first character is drawn from unprocessed at each level
            new_up = up[1:]
            explore(new_p, new_up)
    explore([], arr)
    return ans


if __name__ == '__main__':
    l = [1, 1, 3]
    # ss = subsets(l)
    # print(ss)
    # ss = permutation_dfs(l)
    # print(ss)

    s2 = permutation_pup(l)
    print(s2)