import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-n for n in nums]
        heapq.heapify(self.nums)
        self.k_heap = []
        for _ in range(k - 1):
            heapq.heappush(self.k_heap, -heapq.heappop(self.nums))

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        heapq.heappush(self.k_heap, -heapq.heappop(self.nums))
        heapq.heappush(self.nums, -heapq.heappop(self.k_heap))
        return -self.nums[0]




        
