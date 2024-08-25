from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_q, atlantic_q = deque(), deque()

        for row in range(ROWS):
            pacific_q.append((row, 0))
            atlantic_q.append((row, COLS-1))

        for col in range(COLS):
            pacific_q.append((0, col))
            atlantic_q.append((ROWS-1, col))

        def bfs(ocean_q):
            reachable = set()

            while ocean_q:
                r, c = ocean_q.popleft()
                reachable.add((r, c))
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for rd, cd in directions:
                    rd += r
                    cd += c
                    if (0 <= rd < ROWS and 0 <= cd < COLS and 
                        heights[rd][cd] >= heights[r][c] and 
                        (rd, cd) not in reachable):
                        
                        ocean_q.append((rd, cd))

            return reachable


        pacific_reachable = bfs(pacific_q)
        atlantic_reachable = bfs(atlantic_q)

        return pacific_reachable.intersection(atlantic_reachable)