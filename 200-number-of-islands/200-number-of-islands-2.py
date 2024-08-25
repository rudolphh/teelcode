from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(row, col):
            if row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != '1':
                return
            grid[row][col] = '0'
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for rd, cd in directions:
                dfs(row + rd, col + cd)


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row, col)

        return islands