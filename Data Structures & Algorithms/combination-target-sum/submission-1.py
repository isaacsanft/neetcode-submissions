class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(path, i, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            elif remaining < 0:
                return
            
            for j in range(i, len(nums)):
                path.append(nums[j])
                remaining -= nums[j]
                backtrack(path, i, remaining)
                path.pop()
                remaining += nums[j]
                i += 1
            
        backtrack([], 0, target)

        return result