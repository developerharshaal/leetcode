import math
class Solution:
    def cnt(self, nums, k):
        cnt = 0
        for i in nums:
            cnt += math.ceil(i/k)
        return cnt
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high)//2
            cnt = self.cnt(piles,mid)
            if cnt <= h: high = mid - 1
            else: low = mid + 1
        return low
