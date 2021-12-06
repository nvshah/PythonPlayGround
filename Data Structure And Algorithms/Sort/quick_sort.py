'''
Idea :- after every pass put pivot at correct position
        ( bubble + selection + merge ) mixture concept
          \
          bubble/selection :- put element at correct pos
          merge :- Divide & Conquer

In merge sort though arr is sorted, need to go till base condition
which is not the case for Quick Sort

Inplace, non-Stable

T.C ;- Worst :- O(n^2)
       Avg   :- O(nlg(n))
'''

def quick_sort_1(arr):
    '''
    Quick Sort wo placing the pivot at correct index at each iteration
    Just Divide Array into correct half to be sort
    '''
    def partition_using_mid(s, e):
        '''
        partition the array in such way that first half element is always less than second half element
        GOAL : find the upper bound of left half & lower bound of right half

        :param s: start idx
        :param e: end idx
        :return : u, l   //upper bound of smaller elem & lower bound of larger elem
        '''

        '''
        You wanna divide whole team of players into 
        teamA : team of weak players
        teamB : team of excellent players
        
        Think p1 & p2 as captain of 2 teams & they are in search of players
        p1 start from left end & p2 starts from right end
        at the end 
        all the elem on left of p1 are in team of p1  ( < pivot )
        all the elem on right of p2 are in team of p2 ( > pivot )
        
        At the end
        ( In other words p1 will point to tail of smaller element hoard 
          & p2 will point to tail of larger element hoard 
        )
        
        think at the end p1 will hand his team to p2 & p2 will hand his team to p1
        ie exchange (deal)
        '''

        m = (s + e) // 2  # middle idx
        pivot = arr[m]
        p1, p2 = s, e  # 2 pointer pointing to first & last

        # At the end p1 will be tail of smaller elem hoard
        # & p2 will be head of larger elem hoard

        while p1 <= p2:
            while arr[p1] < pivot:
                p1 += 1
            while arr[p2] > pivot:
                p2 -= 1

            # if arr is sorted than no swapping is needed
            if p1 > p2:
                break
            if p1 < p2:
                arr[p1], arr[p2] = arr[p2], arr[p1]

            p1, p2 = p1+1, p2-1

        return p2, p1  # u, l   // upper bound of left half & lower bound of right half

    def sort(s, e):
        ''' sort the array for elems [s, e] via just only partition & not correct placememt'''
        print(s, e)
        if s >= e:
            return
        if e-s == 1:  # 2 element only
            arr[s], arr[e] = min(arr[s], arr[e]), max(arr[s], arr[e])
            return

        # 1. partition by mid element
        # s.t. left part < right part i.e [s, u] < [l, e]
        u, l = partition_using_mid(s, e)
        sort(s, u) # sort the left part
        sort(l, e) # sort the right part

    sort(0, len(arr)-1)


def quick_sort_2(arr):
    ''' Traditional Quick Sort :- placing pivot at correct place'''

    def partition_by_hoare(s, e):
        '''
        Place pivot to its correct position
        pivot = first index for simplicity
        :param s: start index
        :param e: end index (inclusive)
        :return : pivot correct location


        story :- till ramesh met suresh both of them
                 will try to find customers for each other
                 & make a deal if possible at the end

        so at the end ramesh will point to last customer found by suresh
        & suresh will point to last customer found by ramesh
        p1 := ramesh
        p2 := suresh
        &
        deal = swapping
        NOTE : at the end there will be 1 one wrong person(pivot) find by ramesh
        so that needs to be replaced to neutral side
        & tha wrong person would be pivot

        When p1 has nothing to swap it will go ahead of p2
        & likewise
        when p2 has nothing to swap it will go beyond p1
        '''
        p = s
        pivot = arr[p]
        p1, p2 = s+1, e  # ramesh starts from first & suresh starts from last

        while True:  # till ramesh & suresh cross each other
            # ramesh quest for suresh's customer
            while p1 <= p2 and arr[p1] <= pivot:
                p1 += 1  # till ramesh found one
            # suresh quest for ramesh's customer
            while p1 <= p2 and arr[p2] >= pivot:
                p2 -= 1  # till suresh found one

            if p1 > p2:  # no customers found for deal
                break

            # if both ramesh & suresh found customer for each other
            # then only deal can be made

            if p1 < p2:
                if arr[p1] != arr[p2]:
                    # swap the customers (deal)
                    arr[p1], arr[p2] = arr[p2], arr[p1]

            p1, p2 = p1+1, p2-1

        # swap the pivot (misnomer) to its correct location
        arr[p2], arr[p] = arr[p], arr[p2]

        return p2  # position of pivot

    def sort(s, e):
        '''
        Sort the Array[s:e+1] using Quick sort ie Divide & conquer
        :param s: start index
        :param e: end index (inclusive)
        '''
        print(s, e)
        if s >= e:  # 1 element
            return

        if e-s == 1:  # 2 elements
            arr[s], arr[e] = min(arr[s], arr[e]), max(arr[s], arr[e])
            return

        # 1. place pivot to its correct location in array
        loc = partition_by_hoare(s, e)

        # 2. Sort two halves
        sort(s, loc-1)
        sort(loc+1, e)

    sort(0, len(arr)-1)


if __name__ == '__main__':
    a = [5, 4, 3, 2, 1]
    #a = [3, 8, 5, 4, 1, 2]
    a = [6, 3, 8, 10, 1, 2, 11, 9, 5]

    a = [1,6,2,7,3,8,4,9,5,10]
    a = [90, 8, 3, 2, 1, 5, 10, 3, 2]

    a = [9, 8, 7, 6, 4, 2, 1]
    #quick_sort_1(a)
    quick_sort_1(a)
    print(a)










