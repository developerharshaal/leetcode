class Solution:
    def countDays(self, nums, k):
        n = len(nums)
        cnt = 1
        s = 0
        for i in range(n):
            if s + nums[i] > k:
                cnt += 1
                s = nums[i]
            else:
                s += nums[i]
        return cnt

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high)//2
            if self.countDays(weights, mid) > days: low = mid + 1
            else: high = mid - 1
        return low
        
