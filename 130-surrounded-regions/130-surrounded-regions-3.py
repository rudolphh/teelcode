from collections import deque

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visited_border = set()

        def dfs_border(r, c):
            if (r, c) not in visited_border and -1 < r < rows and -1 < c < cols and board[r][c] == 'O':
                board[r][c] = 'U'
                direction_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for row_off, col_off in direction_offsets: 
                    rd = r + row_off
                    cd = c + col_off
                    dfs_border(rd, cd)

        def switcher(r, c):
            if board[r][c] == 'O':
                dfs_border(r, c)
                board[r][c] = 'U'
                
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