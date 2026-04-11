class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        def dfs(r, c, visit, grid):
            if (r not in range(ROWS) or c not in range(COLS)
                or grid[r][c] == 1 or (r, c) in visit):
                return 0

            if r == ROWS - 1 and c == COLS - 1:
                return 1

            visit.add((r,c))

            count = 0

            count += dfs(r+1, c, visit, grid)
            count += dfs(r-1, c, visit, grid)
            count += dfs(r, c+1, visit, grid)
            count += dfs(r, c-1, visit, grid)

            visit.remove((r,c))

            return count
        return dfs(0, 0, visit, grid)
