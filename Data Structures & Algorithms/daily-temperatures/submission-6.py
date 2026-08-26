class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        next_days = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                index = stack.pop()[1]
                next_days[index] = i - index
            stack.append((temp, i))
        
        return next_days






        