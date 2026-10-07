class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def backtrack(path, row, col):

            if len(path) == len(word):
                return True

            for dr, dc in directions:
                if not (0 <= row + dr < m and 0 <= col + dc < n):
                    continue
                if (row + dr, col + dc) in path:
                    continue
                if board[row + dr][col + dc] != word[len(path)]:
                    continue
                path.append((row + dr, col + dc))
                if backtrack(path, row + dr, col + dc):
                    return True
                path.pop()
            
        
        for row in range(m):
            for col in range(n):
                if board[row][col] != word[0]:
                    continue
                if backtrack([(row, col)], row, col):
                    return True
        return False