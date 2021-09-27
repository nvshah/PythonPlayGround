class Node:
    def __init__(self, val):
        self.val = val

    def child(self, child):
        self.child = child


if __name__ == '__main__':
    root = Node('r')
    left_child = Node('lc')
    right_child = Node('rc')

    root.child(left_child)
    left_child.child(right_child)
    right_child.child(left_child)

    del root         # rc = 0
    del left_child   # rc = 1
    del right_child  # rc = 1