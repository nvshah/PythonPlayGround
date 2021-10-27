import operator as op

# Find the small or big element index

l = [4,5,2,8,9,1,7,0]
b = max(range(len(l)), key=l.__getitem__)
s = min(range(len(l)), key=l.__getitem__)

print('max idx-> ', b, ' min idx-> ', s)  # max idx->  4  min idx->  7

b2 = min(range(len(l)), key=lambda x: op.methodcaller('__getitem__', x)(l))
b1 = max(range(len(l)), key=lambda x: op.methodcaller('__getitem__', x)(l))

print(b1, b2)  # 4  7