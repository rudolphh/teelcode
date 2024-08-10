from collections import deque

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visited = set()

        def bfs_region(r, c):
            current_region = set()
            edge_cell = False

            q = deque()
            q.append((r,c))

            while q:
                row, col = q.popleft()
                current_region.add((row, col))

                if row == 0 or row == rows-1 or col == 0 or col == cols-1:
                    edge_cell = True

                direction_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for row_off, col_off in direction_offsets: 
                    rd = row + row_off
                    cd = col+col_off
                    if (-1 < rd < rows and -1 < cd < cols 
                        and (rd, cd) not in current_region and (rd,cd) not in visited 
                        and board[rd][cd] == 'O'):
                        q.append((rd,cd))
                        current_region.add((rd,cd))

            if not edge_cell:
                for cell_row, cell_col in current_region:
                    board[cell_row][cell_col] = 'X'

        def edgeCell(r, c):
            if r == 0 or r == rows-1 or c == 0 or c == cols-1:
                return True

        for row in range(rows):
            for col in range(cols):
                if not edgeCell(row, col) and (row, col) not in visited and board[row][col] == 'O':
                    bfs_region(row, col)