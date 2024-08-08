from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(row, col):
            q = deque()
            q.append((row, col))

            while q:
                r, c = q.popleft()
                grid[r][c] = '0'

                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for direction_row, direction_col in directions:
                    direction_row += r
                    direction_col += c

                    if (-1 < direction_row < rows and -1 < direction_col < cols and 
                        grid[direction_row][direction_col] == '1'):
                        q.append((direction_row, direction_col))
                        grid[direction_row][direction_col] = '0'

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    islands += 1
                    bfs(row, col)


        return islands