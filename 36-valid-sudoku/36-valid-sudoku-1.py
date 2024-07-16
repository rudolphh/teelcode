class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Initialize sets for rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = collections.defaultdict(set)
        
        # Iterate through each cell in the board
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                # Calculate box index
                #box_index = (r // 3) * 3 + (c // 3)
                
                # Check if the value is already seen in the row, column, or box
                if val in rows[r] or val in cols[c] or val in boxes[(r//3, c//3)]:
                    return False
                
                # Add the value to the sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r//3, c//3)].add(val)
        
        return True