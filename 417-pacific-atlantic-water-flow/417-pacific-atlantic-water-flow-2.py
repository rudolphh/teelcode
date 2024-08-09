
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        result = []
        pacific, atlantic = set(), set()

        def dfs_flow(r, c, ocean, prev_height):
            if (r, c) not in ocean and (-1 < r < rows) and (-1 < c < cols) and heights[r][c] >= prev_height:
                ocean.add((r, c))
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    dfs_flow(dr+r, dc+c, ocean, heights[r][c])

        for col in range(cols):
            dfs_flow(0, col, pacific, heights[0][col])
            dfs_flow(rows-1, col, atlantic, heights[rows-1][col])

        for row in range(rows):
            dfs_flow(row, 0, pacific, heights[row][0])
            dfs_flow(row, cols-1, atlantic, heights[row][cols-1])


        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result