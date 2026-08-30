class Solution:
    def intToIndices(self, num: int, col: int) -> tuple[int]:
        return (num // col, num % col)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        col = len(matrix[0])
        high = len(matrix) * len(matrix[0])

        
        while low < high:
            mid = (low + high) // 2
            indices = self.intToIndices(mid, col)
            
            midpoint = matrix[indices[0]][indices[1]] 

            if midpoint == target:
                return True
            
            elif midpoint < target:
                low = mid + 1
            
            else:
                high = mid
            
        return False
        