from collections import deque

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def bfs_border(r, c):
            current_region = set()

            q = deque()
            q.append((r,c))

            while q:
                row, col = q.popleft()
                if (row, col) not in current_region:
                    current_region.add((row, col))

                direction_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for row_off, col_off in direction_offsets: 
                    rd = row + row_off
                    cd = col+col_off
                    if (-1 < rd < rows and -1 < cd < cols 
                        and (rd, cd) not in current_region and board[rd][cd] == 'O'):
                        board[rd][cd] = 'U'
                        q.append((rd,cd))
                        current_region.add((rd,cd))

        def switcher(r, c):
            if board[r][c] == 'O':
                board[r][c] = 'U'
                bfs_border(r, c)

        for col in range(cols):
            switcher(0, col)
            switcher(rows-1, col)

        for row in range(rows):
            switcher(row, 0)
            switcher(row, cols-1)


        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'U':
                    board[row][col] = 'O'