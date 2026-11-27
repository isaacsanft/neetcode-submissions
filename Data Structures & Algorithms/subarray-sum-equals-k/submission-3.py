from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] += 1
        running_sum = 0
        subarray_count = 0
        n = len(nums)

        for i in range(n):
            running_sum += nums[i]
            subarray_count += freq.get(running_sum - k, 0)            
            freq[running_sum] += 1
        
        return subarray_count
