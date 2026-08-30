class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right = 0
        left = 0
        max_profit = 0

        while left < len(prices) - 1:
            if right < len(prices) - 1 and prices[right] >= prices[left]:
                right += 1
                if prices[right] - prices[left] > max_profit:
                    max_profit = prices[right] - prices[left]

            else:
                left = right
        
        return max_profit
                


        