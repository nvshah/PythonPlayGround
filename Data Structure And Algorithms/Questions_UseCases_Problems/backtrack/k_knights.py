from typing import List

def k_knights(k):
    ''' T.C := O(n^3 + n!)
        O(n^3) = n * O(n^2)  ie n times isSafe Call
        O(n!) = Checking all possibilities ie whilst deducting rows after selection
    '''
    def display(board: List[List[bool]]):
        for r in board:
            for c in r:
                if c:
                    print('♘ ', end='')
                else:
                    print('- ', end='')
            print()

    def isSafe(r, c, board):
        ''' Find if (r,c) cell is safe or not !
            Check - Above Current row Only
            (As we are moving row by row wise)
        '''
        # 2.5 move each time
        moves = [(r-1, c-2), (r-2, c-1), (r-1, c+2), (r-2, c+1)]

        for i, j in moves:
            if 0 <= i and 0 <= j < k:  # Safe on Boundaries
                if board[i][j]:
                    return False
        return True

    def backtrack(board, r, c, remain):
        ''' backtrack while selecting pos of queen at each row (row by row)
            return number of possible ways to place n-queens in n*n boards so that they do not clash each other
            :board : Matrix
            :r : current row number to explore
            :c : current col number to explore
            :remains: remaining number of Knights to be filled in board
        '''

        # Traverse Row By Row (In Row Left => Right )

        if remain == 0:
            # all knight are placed
            display(board)
            print()
            return 1
        if r == k:   # reach last row out of bounds
            return 0
        if c == k:  # col-out-of-bound so move to next row
            return backtrack(board, r+1, 0, remain)

        ways = 0

        # 1. try to place knight at (r,c)
        if isSafe(r, c, board):
            # Place Knight at (r,c)
            board[r][c] = True
            ways += backtrack(board, r, c+1, remain-1)
            # backtrack
            # UnPlace Knight at (r,c)
            board[r][c] = False

        # 2. Exclude (r,c) from search
        ways += backtrack(board, r, c+1, remain)

        return ways

    board = [[False]*k for _ in range(k)]
    return backtrack(board, 0, 0, k)

if __name__ == '__main__':
    w = k_knights(3)
    print(w)