#BRUTE FORCE
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            s = 0
            for j in range(i,n):
                s += nums[j]
                if s == goal: ans += 1
        return ans


#OPTIMAL APPROACH
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(nums, goal):
            if goal < 0: return 0
            l, r = 0, 0
            cnt = 0
            s = 0
            while r < len(nums):
                s += nums[r]
                while s > goal:
                    s -= nums[l]
                    l += 1
                cnt += (r-l+1)
                r += 1
            return cnt

        return atMost(nums, goal) - atMost(nums, goal-1)
