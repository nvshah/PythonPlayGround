# --- 1 generator and truthiness -----

seq = (i for i in range(5))
l = list(seq)
print(l)
# seq is consumed entirely now
print(all(seq))  # True  (because by default an obj is True, until __bool__ or __len__ is wishing)


# --- 2 Custom Object
class C1:
    def __bool__(self):
        return False

    def __len__(self):
        return 0

class CustomSeq:
    def __init__(self, n):
        self.n = n

    # -> Iterator Protocol (len, getitem)
    def __len__(self):
        return self.n
    def __getitem__(self, item):
        return None


print(bool(C1()))  # False (=> len(C1()) == 0)

c1 = CustomSeq(1)
c2 = CustomSeq(0)
print(all([c1, c2]))  # False (=> c2 is seq with length 0)


