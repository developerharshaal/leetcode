class Solution:
    def helper(self, ds, ans, k, n, start):
        if len(ds)==k:
            if n == 0: ans.append(ds.copy())
            return
        for i in range(start, 10):
            ds.append(i)
            self.helper(ds, ans, k, n-i, i+1)
            ds.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        ds = []
        self.helper(ds, ans, k, n, 1)
        return ans
