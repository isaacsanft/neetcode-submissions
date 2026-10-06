class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        money_2_back = nums[0]
        money_1_back = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            curr = max(money_1_back, money_2_back + nums[i])
            money_1_back, money_2_back = curr, money_1_back

        return money_1_back
        