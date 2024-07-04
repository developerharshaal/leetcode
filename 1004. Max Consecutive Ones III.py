#BRUTE FORCE
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxl = 0
        for i in range(n):
            zero = 0
            for j in range(i,n):
                if nums[j] == 0:
                    zero += 1
                if zero <= k:
                    l = j - i + 1
                    maxl = max(maxl, l)
                else:
                    break
        return maxl

#BETTER APPROACH
    class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxl = 0
        l, r = 0, 0
        zero = 0
        while r < len(nums):
            if nums[r] == 0: zero += 1
            while zero > k:
                if nums[l] == 0: l -= 1
            if zero <= k:
                maxl = max(maxl, r-l+10)
            r += 1
        return maxl

#OPTIMAL APPROACH
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        maxl = 0
        zero = 0
        while r < len(nums):
            if nums[r] == 0: zero += 1
            if zero > k:
                if nums[l] == 0: zero -= 1
                l += 1
            if zero <= k:
                maxl = max(maxl, r-l+1)
            r += 1
        return maxl
