class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        cols = set()
        diag_pos = set()
        diag_neg = set()
        
        def build_result(queens):
            result = ["" for _ in range(n)]
            for r, c in queens:
                row = "." * c + "Q" + "." * (n - c - 1)
                result[r] = row
            return result
        
        def backtrack(queens, r):
            if r == n:
                results.append(build_result(queens))
                return
            
            for c in range(n):
                if c in cols or (r + c) in diag_pos or (r - c) in diag_neg:
                    continue

                cols.add(c)
                diag_pos.add(r + c)
                diag_neg.add(r - c)
                queens.append((r, c))

                backtrack(queens, r + 1)

                cols.remove(c)
                diag_pos.remove(r + c)
                diag_neg.remove(r - c)
                queens.pop()
    
        backtrack([], 0)
        
        return results