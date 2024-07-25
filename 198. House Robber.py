# RECUSRIVE APPROACH
class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(ind):
            if ind < 0 : return 0
            if ind == 0: return nums[0]
            if ind == 1: return max(nums[0], nums[1])
            pick = nums[ind] + solve(ind-2)
            notpick = solve(ind-1)
            return max(pick, notpick)
        return solve(len(nums)-1)

# MEMOIZATION
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def solve(ind, dp):
            if ind < 0 : return 0
            if dp[ind] != -1: return dp[ind]
            pick = nums[ind] + solve(ind-2, dp)
            notpick = solve(ind-1, dp)
            dp[ind] = max(pick, notpick)
            return dp[ind]
        dp = [-1] * n
        if n == 0: return 0
        return solve(n-1, dp)

# TABULATION
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]
