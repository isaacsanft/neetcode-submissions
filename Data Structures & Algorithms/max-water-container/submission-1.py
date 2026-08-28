class Solution:

    def maxArea(self, heights: List[int]) -> int:

        maxWater = 0
        left = 0
        right = len(heights) - 1

        def area():
            return min(heights[left], heights[right]) * (right - left)

        if area() > maxWater:
            maxWater = area()
        while left < right :
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            elif heights[left] == heights[right]:
                right -= 1
                left += 1
            if area() > maxWater:
                maxWater = area()


        return maxWater
            

        
        