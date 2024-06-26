class Solution:
    def isSafe(self, row, col, board, n):
        drow = row
        dcol = col

        while row >= 0 and col >= 0:
            if board[row][col] == 'Q': return False
            row -= 1
            col -= 1

        row = drow
        col = dcol
        while col >= 0:
            if board[row][col] == 'Q': return False
            col -= 1

        row = drow
        col = dcol
        while col >= 0 and row < n:
            if board[row][col] == 'Q': return False
            col -= 1
            row += 1

        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.'] * n for _ in range(n)]  
        def backtrack(col):
            if col == n:
                ans.append([''.join(row) for row in board])
                return

           
            for row in range(n):
                if self.isSafe(row, col, board, n):
                    board[row][col] = 'Q'
                    backtrack(col+1)
                    board[row][col] = '.'
            
        backtrack(0)
        return ans
