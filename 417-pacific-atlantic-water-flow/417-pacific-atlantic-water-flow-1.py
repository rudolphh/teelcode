
###  FAILED - does not work (close but no cigar)
#  see solution -2

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        result = []
        pacific = set()

        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    pacific.add((row, col))
                elif heights[row][col] >= heights[row][col-1]:
                    pacific.add((row, col))
                else:
                    break

        for col in range(cols):
            for row in range(rows):
                if row == 0 or col == 0:
                    continue
                elif heights[row][col] >= heights[row-1][col]:
                    pacific.add((row, col))
                else:
                    break

        for row in range(rows):
            for col in range(cols-1, -1, -1):
                if row == (rows-1) or col == (cols-1):
                    if (row, col) in pacific:
                        result.append((row, col))

                elif heights[row][col] >= heights[row][col+1] and (row, col) in pacific:
                    result.append((row, col))
                else:
                    break


        for col in range(cols):
            for row in range(rows-1, -1, -1):
                if row == (rows-1) or col == (cols-1):
                    continue
                elif heights[row][col] >= heights[row+1][col] and (row, col) in pacific:
                    result.append((row, col))
                else:
                    break

        print(pacific)
        return result