def doTransposeOf(mat):
    '''
    Inplace Transpose i.e m[i][j] = m[j][i]
    '''
    r = len(mat)
    for i in range(r):
        for j in range(i, r):
            mat[i][j] = mat[j][i] # Swap
    return mat


def reverseBy2Pointer(l):
    '''inplace'''
    for i in range(len(l) // 2):
        l[i], l[-i-1] = l[-i-1], l[i]  # Swap
    return l


l = [1,2,3,4,5]
print(reverseBy2Pointer(l))