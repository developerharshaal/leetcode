class Solution:
    def poss(self, nums, days, m, k):
        cnt = 0
        numB = 0
        for i in nums:
            if i <= days: cnt += 1
            else: 
                numB += (cnt//k)
                cnt = 0
        numB += (cnt//k)
        return numB >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1
        low = min(bloomDay)
        high = max(bloomDay)+1
        while low <= high:
            mid = (low + high)//2
            if not self.poss(bloomDay, mid, m, k): low = mid + 1
            else: high = mid - 1
        return low            
