class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(path, i):
            if sum(path) == target:
                result.append(path[:])
                return
            elif sum(path) > target:
                return
            
            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(path, i)
                path.pop()
                i += 1
            
        backtrack([], 0)

        return result