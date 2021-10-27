import operator as op


def doTransposeOf(mat):
    '''
    Inplace Transpose i.e m[i][j] = m[j][i]
    '''
    r = len(mat)
    for i in range(r-1):
        for j in range(i+1, r):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j] # Swap


def reverseBy2Pointer(l):
    '''inplace'''
    for i in range(len(l) // 2):
        l[i], l[-i-1] = l[-i-1], l[i]  # Swap
    return l

# Find the small or big element index

l = [4,5,2,8,9,1,7,0]
b = max(range(len(l)), key=l.__getitem__)
s = min(range(len(l)), key=l.__getitem__)

print('max idx-> ', b, ' min idx-> ', s)  # max idx->  4  min idx->  7

b2 = min(range(len(l)), key=lambda x: op.methodcaller('__getitem__', x)(l))
b1 = max(range(len(l)), key=lambda x: op.methodcaller('__getitem__', x)(l))

print(b1, b2)  # 4  7


l = [1,2,3,4,5]
print(reverseBy2Pointer(l))