# RECURSION
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

# MEMOIZATION
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)

    def helper(self, n, memo):
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]


# TABULATION
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1: return 1
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# SPACE OPTIMIZATION
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1: return 1
        prev, curr = 1, 1
        for i in range(2,n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr
