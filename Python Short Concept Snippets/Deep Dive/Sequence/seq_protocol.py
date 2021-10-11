class CustomSeq:
    def __init__(self, n):
        self.n = n

    # -> Iterator Protocol (len, getitem)
    def __len__(self):
        return self.n

    def __getitem__(self, item):
        return None