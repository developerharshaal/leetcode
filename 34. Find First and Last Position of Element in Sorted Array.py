class Solution:
    def lower(self, nums, n ,x):
        low, high = 0, n - 1
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def upper(self, nums, n, x):
        low, high = 0, n - 1
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans-1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lower(nums, len(nums), target)
        if (lb == len(nums) or nums[lb] != target):
            return [-1,-1]
        else:
            return [lb,self.upper(nums, len(nums), target)]
