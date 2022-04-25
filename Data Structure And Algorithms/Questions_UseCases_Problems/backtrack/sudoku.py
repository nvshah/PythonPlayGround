from math import isqrt
from operator import itemgetter
from typing import List
from collections import defaultdict
from string import digits


def sudoku_solver(board):
    rows, cols = len(board), len(board[0])
    square_size = isqrt(rows)

    def display(grid):
        for row in grid:
            for num in row:
                print(num, end=' ')
            print()

    def isSafe(grid, r, c, n):
        '''
        Can a num {n} be put at (r,c) on grid
        :param grid: composed of diff squares
        :param r: row
        :param c: col
        :param n: number
        :return:
        '''
        # Rule :- there can be no duplication of numbers 1-9 within each square (or row or column).

        # 1. Check if {n} already present in row or col
        if (n in grid[r]) or (n in map(itemgetter(c), grid)):
            return False

        # 2. Check if duplicates exists in corresponding Square
        # find rowStart & colStart for corresponding Square
        rowStart = r - (r % square_size)
        colStart = c - (c % square_size)

        for i in range(rowStart, rowStart + square_size):
            for j in range(colStart, colStart + square_size):
                if grid[i][j] == n:
                    return False

        return True

    def solve(grid):
        i, j = -1, -1

        # 1. Check for any empty element
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    i, j = row, col
                    break
            else:
                continue  # cannot find empty cell in curr row so look for next row
            break
        else:
            return True  # No Empty Cell found in grid (=> Sudoku Solved)

        # 2. Solve the (i, j)
        for n in range(1, 10):
            if isSafe(grid, i, j, n):
                # place {n} at (i,j)
                grid[i][j] = n
                # EXPLORE for next Empty Cell
                if solve(grid):
                    return True
                # BACKTRACK unable to solve with this number {n} at (i,j) so remove {n}
                grid[i][j] = 0

        return False

    if solve(board):
        display(board)


def solveSudoku(board: List[List[int]]) -> None:
    """
    iNplace
    """
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    digit = set(range(1, 10))

    for r in range(9):
        for c in range(9):
            if board[r][c] == 0: continue  # as need to record for filled vals only
            v = board[r][c]

            # record vals of row, col, sqr
            rows[r].add(v)
            cols[c].add(v)
            squares[(r // 3, c // 3)].add(v)

    def backtrack(r, c):
        if r == 9:
            return True  # all row are traversed
        if c == 9:
            return backtrack(r + 1, 0)  # move to next row

        if board[r][c] != 0:  # already filled
            return backtrack(r, c + 1)

        i, j = r // 3, c // 3  # square coordinates
        valid_digits = digit - {*rows[r], *cols[c], *squares[(i, j)]}

        # try placing each digit in curr cell
        for d in valid_digits:
            # 1. record vals of row, col, sqr
            rows[r].add(d)
            cols[c].add(d)
            squares[(i, j)].add(d)
            board[r][c] = d  # place the digit {d} at (r,c) in board

            # 2. Explore next
            res = backtrack(r, c + 1)

            if res: return True  # {d} at (r,c) is correct choice

            # 3. BackTrack  -> {d} at (r,c) is incorrect; try placing diff digit {d`}
            #    First Undo Prev Choice (before moving to next)
            board[r][c] = 0
            rows[r].remove(d)
            cols[c].remove(d)
            squares[(i, j)].remove(d)

        return False

    backtrack(0, 0)

    print(board)


if __name__ == '__main__':
    grid = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    #sudoku_solver(grid)

    '''  (Output)
    4 8 7 6 2 9 5 3 1 
    2 6 3 4 1 5 9 8 7 
    9 7 4 8 6 3 1 2 5 
    8 5 1 7 9 2 6 4 3 
    1 3 8 9 4 7 2 5 6 
    6 9 2 3 5 1 8 7 4 
    7 4 5 2 8 6 3 1 9 
    '''

    solveSudoku(grid)
