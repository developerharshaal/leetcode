class Solution:
    def isPalin(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start +=1
            end -= 1
        return True

    
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        ds = []

        def backtrack(ind):
            if ind == len(s):
                ans.append(ds.copy())
                return

            for i in range(ind, len(s)):
                if self.isPalin(s, ind, i):
                    ds.append(s[ind:i+1])
                    backtrack(i+1)
                    ds.pop()

        backtrack(0)
        return ans
