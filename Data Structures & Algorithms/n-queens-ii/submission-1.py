class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        board = [["."] * n for i in range(n)]

        cols = set()
        posDiag = set()
        negDiag = set()

        def dfs(r):
            nonlocal res
            if r == n:
                res += 1
                return 
            for c in range(n):
                if c in cols or r+c in posDiag or r-c in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                dfs(r+1)

                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        dfs(0)
        return res