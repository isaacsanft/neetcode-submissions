from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = defaultdict(int)
        topK = []

        for number in nums:
            counts[number] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():
            buckets[freq].append(num)

        
        for bucket in reversed(buckets):
            for element in bucket:
                topK.append(element)
                if len(topK) == k:
                    return topK
                    




        

            
        