class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(path, i, remaining):
            if remaining == 0:
                result.append(path[:])
                
            elif remaining < 0:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])
                remaining -= candidates[j]
                backtrack(path, j + 1, remaining)
                path.pop()
                remaining += candidates[j]
            
        backtrack([], 0, target)

        return result
        