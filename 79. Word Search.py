class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        path = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= n or c >= m or
                word[i] != board[r][c] or
                (r,c) in path):
                return False

            path.add((r,c))
            res = (backtrack(r+1,c,i+1) or
                    backtrack(r-1,c,i+1) or
                    backtrack(r,c+1,i+1) or
                    backtrack(r,c-1,i+1))

            path.remove((r,c))
            return res
        
        for i in range(n):
            for j in range(m):
                if backtrack(i,j,0):
                    return True
        return False
