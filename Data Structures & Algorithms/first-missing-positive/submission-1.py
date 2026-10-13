class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        while i < n:
            num = nums[i]
            if 1 <= num <= n and nums[num - 1] != num:
                nums[num - 1], nums[i] = nums[i], nums[num - 1]
                continue
            i += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
        