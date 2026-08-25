from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = defaultdict(set) # row (int) - key, seen_set - value
        column_check = defaultdict(set) # col (int) - key, seen_set - value
        box_check = defaultdict(set) # box tuple(0-2, 0-2) key, seen_set - value

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                box = (r // 3, c // 3)

                if value in row_check[r] or value in column_check[c] or value in box_check[box]:
                    return False

                if value != ".":
                    row_check[r].add(value)
                    column_check[c].add(value)
                    box_check[box].add(value)
        
        return True


'''
        for i in range(9): # verifying rows
            seen = set()
            for j in range(9):
                if board[i][j] in seen and board[i][j] != ".":
                    return False
                seen.add(board[i][j])
        
        for j in range(9): # verifying columns
            seen = set()
            for i in range(9):
                if board[i][j] in seen and board[i][j] != ".":
                    return False
                seen.add(board[i][j])

        box_buffer = [0, 3, 6]

        for row_buffer in box_buffer: # verifying boxes
            for column_buffer in box_buffer:
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[row_buffer + i][column_buffer + j] in seen and board[row_buffer + i][column_buffer + j] != ".":
                            return False
                        seen.add(board[row_buffer + i][column_buffer + j])
        
        return True
'''



