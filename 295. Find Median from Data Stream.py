class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)

        if (self.small and self.large and (-self.small[0]) > self.large[0]):
            val = -heappop(self.small)
            heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heappop(self.large)
            heappush(self.small, -val)

        if len(self.small) > len(self.large) + 1:
            val = -heappop(self.small)
            heappush(self.large, val)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]

        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        return (-1 * self.small[0] + self.large[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
