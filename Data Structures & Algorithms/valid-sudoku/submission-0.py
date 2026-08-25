class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        i = 0 # row index
        j = 0 # column index

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



