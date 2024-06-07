class Solution:
    def nth_row(self, n: int) -> List[int]:
        res = []
        ans = 1
        res.append(ans)
        for i in range(1,n):
            ans=ans*(n-i)//i
            res.append(ans)
        return res
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append(self.nth_row(i+1))
        return res
