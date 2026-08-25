from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = defaultdict(int)
        topK = []

        for number in nums:
            counts[number] += 1

        buckets = [[] for _ in range(len(nums))]

        for key, value in counts.items():
            buckets[value - 1].append(key)

        
        for bucket in reversed(buckets):
            for element in bucket:
                topK.append(element)
                if len(topK) == k:
                    return topK
                    




        

            
        