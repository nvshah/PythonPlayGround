'''
1. Count To reach Maze from Top left to Bottom Right
   Only Right & Down option are available to Move

   rows start from n -> 1
   cols start from n -> 1

   So top left = (n,n)
      bottom right = (1,1)
'''
import math
from pprint import pprint


def maze(r, c):
    '''
    find the number of ways through which you can reach bottom-right from given cell-number in maze
    :param r: row number
    :param c: col number
    :return: count ie #diff ways to reach bottom-right cell (ie (1,1))
    '''
    if r == 1 or c == 1:
        return 1  # there is only 1 way via which you can reach bottom right from last column or last row

    bottom = maze(r-1, c)
    right = maze(r, c-1)

    return bottom + right

def print_path(r, c):
    def find(p, r, c):
        '''
        find the possible path to reach bottom right cell (ie (1,1))
        :param p: path
        :param r: row
        :param c: col
        :return: none
        '''
        if r == 1 and c == 1:
            print(p)

        if r > 1: # go bottom
            find(p+'B', r-1, c)

        if c > 1: # go right
            find(p+'R', r, c-1)
    find('', r, c)

def get_paths(r,c):
    def find(p, r, c):
        '''
        find the possible path to reach bottom right cell (ie (1,1))
        :param p: path
        :param r: row
        :param c: col
        :return: none
        '''
        if r == 1 and c == 1:
            return [p]

        paths = []

        if r > 1 and c > 1: # go diagonally
            lst = find(p+'D', r-1, c-1)
            paths.extend(lst)

        if r > 1: # go bottom
            lst = find(p+'B', r-1, c)
            paths.extend(lst)

        if c > 1: # go right
            lst = find(p+'R', r, c-1)
            paths.extend(lst)

        return paths

    return find('', r, c)

# ---------------------------

'''
 1. Normal Matrix Onwards ie
     top-left = (1,1)
     bottom-right = (n,n)
'''

def printAllPath(r, c):
    board = [[0]*c for _ in range(r)]
    visit = [[False]*c for _ in range(r)]

    def find(i, j, path, step):
        if i == r-1 and j == c-1:  # reach bottom right
            print(f'{path=}')
            board[i][j] = step
            for row in board:
                print(row)
            print()  # space after board
            return

        # if visited this
        if visit[i][j]: return

        # Explore (include current)
        board[i][j] = step
        visit[i][j] = True

        # top
        if i > 0:
            find(i-1, j, path+'T', step+1)

        # right
        if j < c-1:
            find(i, j+1, path+'R', step+1)

        # down
        if i < r-1:
            find(i+1, j, path+'B', step+1)

        # left
        if j > 0:
            find(i, j-1, path+'L', step+1)

        # Backtrack (Exclude current)
        board[i][j] = 0
        visit[i][j] = False

    find(0, 0, '', 1)


def uniquePaths2(m: int, n: int) -> int:
    return math.comb(m+n-2, m-1)


if __name__ == '__main__':
    # print(maze(3,3))
    # ps = get_paths(3,3)
    # print(ps)

    printAllPath(3, 3)
