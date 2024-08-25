
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        pacific, atlantic = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, prev, ocean):
            if 0 <= r < ROWS and 0 <= c < COLS and heights[r][c] >= prev and (r, c) not in ocean:
                ocean.add((r, c))
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for rd, cd in directions:
                    dfs(r + rd, c + cd, heights[r][c], ocean)

        for row in range(ROWS):
            dfs(row, 0, heights[row][0], pacific)
            dfs(row, COLS-1, heights[row][COLS-1], atlantic)

        for col in range(COLS):
            dfs(0, col, heights[0][col], pacific)
            dfs(ROWS-1, col, heights[ROWS-1][col], atlantic)

        coordinates = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    coordinates.append((row, col))

        return coordinates