class Solution:
    def countSum(self, nums, mid):
        cnt = 1
        s = 0
        for i in range(len(nums)):
            if s + nums[i] <= mid: s += nums[i]
            else:
                cnt += 1
                s = nums[i]
        return cnt 

    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k: return -1
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high)//2
            val = self.countSum(nums, mid)
            if val > k: low = mid + 1
            else: high = mid - 1
        return low
