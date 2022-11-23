import timeit
'''
LIST TIPS
'''

#1. ----------------------------

l = [1,2,3]

l[:] = [x**2 for x in l]  #
l = [x**2 for x in l]

def t1():
    # Surprisingly this is slower
    l = [1,2,3,4,5]
    l = [x**2 for x in l]

def t2():
    #Surprisingly this is faster
    l = [1,2,3,4,5]
    l[:] = [x**2 for x in l]


#print(timeit.timeit("l[:] = [x**2 for x in l]", "from __main__ import l", number=10))  #2.796999999998828e-06
#print(timeit.timeit("l = [x**2 for x in l]", "from __main__ import l", number=10))  #1.0460000000010738e-06

print(timeit.timeit(t1, number=10))  # 3.8018000000000773e-05
print(timeit.timeit(t2, number=10))  # 3.085399999999683e-05


#2--------------------------------

l = [1,2,3,4,5,6,7,8,9,0]

print(id(l))

l[:] = [x for x in l if not x % 2]  # Inplace modifications

print(id(l))


#3---------------------------------

'''
String Tips : 
'''

s = "NipunShah"
print(s.startswith("Nipun"))   # Correct
print(s[:4] == "Nipun")        # Not Preferred

#4---------------------------------

# Find the string with largest length
l = ['he', 'nipun', 'charusat']
a = max(l, key=len, default='')  # default is useful when l is empty
