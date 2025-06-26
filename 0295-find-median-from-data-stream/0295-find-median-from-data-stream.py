class MedianFinder:

    def __init__(self):
        self.lower_eles = []
        self.upper_eles = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower_eles, -num)
        heapq.heappush(self.upper_eles, -heapq.heappop(self.lower_eles))

        if len(self.upper_eles) > len(self.lower_eles):
            heapq.heappush(self.lower_eles, -heapq.heappop(self.upper_eles))
    def findMedian(self) -> float:
        if len(self.lower_eles) > len(self.upper_eles):
            return -self.lower_eles[0]
        else:
            return (-self.lower_eles[0] + (self.upper_eles[0])) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()