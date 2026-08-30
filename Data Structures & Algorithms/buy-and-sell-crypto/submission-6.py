class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right = 1
        left = 0
        max_profit = 0

        while right < len(prices):
            if prices[right] >= prices[left]:
                if prices[right] - prices[left] > max_profit:
                    max_profit = prices[right] - prices[left]
                right += 1

            else:
                left = right
        
        return max_profit