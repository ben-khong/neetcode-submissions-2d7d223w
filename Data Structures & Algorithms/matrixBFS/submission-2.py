class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        visit.add((0,0))
        q.append((0,0))
        length = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                if (row == ROWS - 1 and col == COLS - 1):
                    return length
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for cr, cc in directions:
                    newRow, newCol = row + cr, col + cc
                    if (newRow not in range(ROWS) or newCol not in range(COLS)
                        or grid[newRow][newCol] == 1 or (newRow, newCol) in visit):
                        continue
                    visit.add((newRow,newCol))
                    q.append((newRow,newCol))
            length += 1
        return -1

