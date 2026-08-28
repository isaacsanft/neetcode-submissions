class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums) < 3:
            return []
        
        triplets = set()

        for anchor in range(len(nums) - 2):
            left = anchor + 1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[anchor] + nums[left] + nums[right]
                if three_sum == 0:
                    triplets.add((nums[anchor], nums[left], nums[right]))
                    left += 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return list(triplets)

        