class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost) - 1

        def dp(n: int) -> int:
            if n == 0:
                return cost[0]
            elif n == 1:
                return cost[1]
            if n in memo:
                return memo[n]
            memo[n] = min(dp(n - 2), dp(n - 1)) + cost[n]
            return memo[n]
        
        return min(dp(n), dp(n - 1))
        