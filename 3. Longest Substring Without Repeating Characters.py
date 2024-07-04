#BRUTE FORCE APPROACH
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxl = 0
        for i in range(n):
            has = defaultdict()
            for j in range(i,n):
                if s[j] in has:
                    break
                l = j - i + 1
                maxl = max(maxl, l)
                has[s[j]] = 1
        return maxl



#OPTIMAL SOLUTION
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, maxl = 0, 0, 0
        n = len(s)
        mpp = {}
        while r < n:
            if s[r] not in mpp or mpp[s[r]] < l:
                mpp[s[r]] = r
                maxl = max(maxl, r-l+1)
            else:
                l = mpp[s[r]] + 1
                mpp[s[r]] = r
            r += 1
        return maxl
