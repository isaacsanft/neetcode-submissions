import heapq

class MedianFinder:

    def __init__(self):
        self.bottom = [float('inf')] # max heap
        self.top = [float('inf')] # min heap

    def addNum(self, num: int) -> None:
        mid_low = -self.bottom[0]
        mid_high = self.top[0]
        if mid_low <= num <= mid_high:
            if len(self.bottom) < len(self.top):
                heapq.heappush(self.bottom, -num)
            else:
                heapq.heappush(self.top, num)
        elif num < mid_low:
            if len(self.bottom) > len(self.top):
                heapq.heappush(self.top, -heapq.heappop(self.bottom))
            heapq.heappush(self.bottom, -num)
        elif mid_high < num:
            if len(self.bottom) < len(self.top):
                heapq.heappush(self.bottom, -heapq.heappop(self.top))
            heapq.heappush(self.top, num)

    def findMedian(self) -> float:
        if len(self.bottom) < len(self.top):
            return self.top[0]
        elif len(self.bottom) > len(self.top):
            return -self.bottom[0]
        return (-self.bottom[0] + self.top[0]) / 2