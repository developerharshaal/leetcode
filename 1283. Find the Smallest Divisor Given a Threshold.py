import math
class Solution:
    def findSum(self, nums, k):
        n = len(nums)
        s = 0
        for i in nums:
            s += math.ceil(i/k)
        return s 
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        while low <= high:
            mid = (low + high)//2
            val = self.findSum(nums, mid)
            if val > threshold: low = mid + 1
            else: high = mid - 1
        return low
