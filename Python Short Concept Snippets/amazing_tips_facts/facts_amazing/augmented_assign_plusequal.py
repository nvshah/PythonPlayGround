import sys


def plus_equals_meaning(x, y):
    # x += y
    res = x.__iadd__(y)
    x = res

    # x[0]
    res = x[0].__iadd__(y)  # calls __getitem__
    x[0] = res   # calls __setitem__

    # x.val += y
    res = x.val.__iadd__(y)
    x.val = res


def plus_equal_may_change_pointer():
    # For Immutable it changes the pointer
    x = 1
    print(id(x))
    x += 1
    print(id(x), "changed")

    # For Mutable It does inplace operation
    l = [1,2]
    print(id(x))
    l += [3]
    print(id(l), "not changed")


def append_to_list(l):
    l += [8,9,10]


if __name__ == '__main__':
    # # amazing obs
    # l = [1,2,3]
    # l += [4,5]
    # append_to_list(l)
    # print(l)  # [1, 2, 3, 4, 5, 8, 9, 10]

    # ------------------ AMAZING plus equal case
    t = ([1,2,3], [4,5,6])
    try:
        t[0] += ['1','2','3']  # concatenation will take place but setter will fail as tuple assignment is not allowed
    #except TypeError:
    except :
        print(sys.exc_info()[0], 'Happens')  # TypeError

    print(t[0]) # [1, 2, 3, '1', '2', '3']

