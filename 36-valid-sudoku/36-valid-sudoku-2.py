class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Initialize sets for rows, columns, and boxes

        seen = collections.defaultdict(set)
        
        # Iterate through each cell in the board
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                # Calculate box index
                #box_index = (r // 3) * 3 + (c // 3)
                
                # Check if the value is already seen in the row, column, or box
                if (r, 'row', val) in seen[r] or (c, 'col', val) in seen[c] or ((r//3, c//3), 'box', val) in seen[(r//3, c//3)]:
                    return False
                
                # Add the value to the sets
                seen[r].add((r, 'row', val))
                seen[c].add((c, 'col', val))
                seen[(r//3, c//3)].add(((r//3, c//3), 'box', val))
        
        return True