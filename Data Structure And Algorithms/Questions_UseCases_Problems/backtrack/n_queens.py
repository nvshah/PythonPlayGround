from typing import  List

def n_queens_1(n):
    ''' T.C := O(n^3 + n!)
        O(n^3) = n * O(n^2)  ie n times isSafe Call
        O(n!) = Checking all possibilities ie whilst deducting rows after selection
    '''
    def display(board: List[List[bool]]):
        for r in board:
            for c in r:
                if c:
                    print('♕ ', end='')
                else:
                    print('- ', end='')
            print()

    def isSafe(r, c, board):
        ''' Find if (r,c) cell is safe or not !
            Check - Vertically Baove & Diagonally Left & Right
            As we are going row by row so we will check 3 directions above the current row
            (as below rows there is no Queen Placed yet)
        '''
        # Above Vertical
        for i in range(r):
            if board[i][c]:
                return False

        # Check Above Left Diagonal
        maxLeft = min(r, c)  # max possible steps in left-Diagonal
        for i in range(1, maxLeft+1):
            if board[r-i][c-i]:
                return False

        # Check Above Right Diagonal
        maxRight = min(r, n-1-c)  # max possible steps in Right-Diagonal
        for i in range(1, maxRight+1):
            if board[r-i][c+i]:
                return False

        # No queen exists in Diagonal & Vertical Path
        return True

    def backtrack(board, row):
        ''' backtrack while selecting pos of queen at each row (row by row)
            return number of possible ways to place n-queens in n*n boards so that they do not clash each other
            :return :- #ways
        '''
        if row == n:
            # all queens are placed in each row
            display(board)
            print()
            return 1

        ways = 0  # total possible ways

        # Explore this {row}
        for col in range(n):
            if isSafe(row, col, board):
                board[row][col] = True  # Pick
                ways += backtrack(board, row+1)  # Explore (next rows)
                board[row][col] = False  # BackTrack

        return ways

    board = [[False]*n for _ in range(n)]
    return backtrack(board, 0)


def n_queens_2(n: int) -> List[List[str]]:
    ''' T.C = O(n!) '''
    board = [['.']*n for _ in range(n)]

    # Below sets keep tracks of respective acquired columns, pos-diag, neg-diag by Queens
    cols = set()  # columns acquired by queens
    pos_diags = set() # defined by (r-c)
    neg_diags = set() # defined by (r+c)

    res = []  # result set keep track of all possible boards

    def backtrack(r):
        if r == n:  # all rows are explored
            res.append(board)
            for r in board:
                print(r)
            print()
            return

            # Explore each column of current row where Queen can be placed
        for c in range(n):
            # 1. find the positive & negative diagonal number this cell (r, c) belongs to.
            diagP, diagN = r-c, r+c

            # 2. check if an Queen Exists already in any of Column, or Diagonal
            #    (Note : not checking of Row as we are already traversing Row by Row placing single Queen)
            #    ( Is Safe )
            if (c in cols) or (diagN in neg_diags) or (diagP in pos_diags):
                continue # Queen cannot be placed at (r,c)

            # 3. place Queen at (r,c)
            board[r][c] = 'Q'
            #    register acquirance
            cols.add(c)
            pos_diags.add(diagP)
            neg_diags.add(diagN)

            # 4. Explore next row (where Queen can be placed in next Row ??) via Recurssion
            backtrack(r+1)

            # 5. BackTrack
            #    remove Queen at (r,c)
            board[r][c] = '.'
            #    un-register acquirance
            cols.remove(c)
            pos_diags.remove(diagP)
            neg_diags.remove(diagN)

    backtrack(0)  # start from first row
    return res



if __name__ == '__main__':
    #ways = n_queens_2(4)
    w = n_queens_1(5)
    print('Total Ways : \n', w)



