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