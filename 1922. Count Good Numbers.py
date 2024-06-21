class Solution:
    
    def pow(self, x, y):
        MOD = 10 ** 9 + 7
        if y == 0: return 1
        ans = self.pow(x, y//2)
        ans = ans * ans
        ans = ans % MOD
        if y % 2: ans = ans * x
        ans = ans % MOD
        return ans
    def countGoodNumbers(self, n: int) -> int:
        odd = n//2
        even = n//2 + (n%2)
        return self.pow(5,even)*self.pow(4,odd) % (10**9 + 7)
