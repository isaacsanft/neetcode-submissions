import math

class Solution:
    def isValid(self, piles: List[int], h: int, k: int) -> bool:
        for pile in piles:
            h -= math.ceil(pile / k)
            if h < 0:
                return False
        return True


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if self.isValid(piles, h, mid):
                right = mid
            else:
                left = mid + 1
        
        return left        