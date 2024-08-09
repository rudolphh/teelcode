from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            nonlocal max_area
            q = deque()
            q.append((r, c))
            area = 0

            while q:
                row, col = q.popleft()
                grid[row][col] = -1
                area += 1

                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for direction_row, direction_col in directions:
                    direction_row += row
                    direction_col += col

                    if (-1 < direction_row < rows and -1 < direction_col < cols and 
                        grid[direction_row][direction_col] == 1):
                        q.append((direction_row, direction_col))
                        grid[direction_row][direction_col] = -1

            max_area = max(max_area, area)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    bfs(r, c)

        return max_area