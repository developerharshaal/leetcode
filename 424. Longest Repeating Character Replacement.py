#BRUTE FORCE
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxl = 0
        for i in range(n):
            mpp = [0] * 26
            maxf = 0
            for j in  range(i,n):
                mpp[ord(s[j]) - ord('A')] += 1
                maxf = max(maxf, mpp[ord(s[j]) - ord('A')])
                changes = (j-i+1) - maxf
                if changes <= k: maxl = max(maxl, j-i+1)
                else: break
        return maxl


#BETTER APPROACH
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxl = 0
        maxf = 0
        l, r = 0, 0
        mpp = [0] * 26
        while r < n:
            mpp[ord(s[r]) - ord('A')] += 1
            maxf = max(maxf, mpp[ord(s[r]) - ord('A')])
            while ((r-l+1)-maxf) > k:
                mpp[ord(s[l]) - ord('A')] -= 1
                maxf = 0
                for i in range(26): maxf = max(maxf, mpp[i])
                l += 1
            if ((r-l+1) - maxf) <= k:
                maxl = max(maxl, r-l+1)

            r += 1

        return maxl


#OPTIMAL APPROACH
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxl = 0
        l, r = 0, 0
        mpp = [0] * 26
        maxf = 0
        while r < len(s):
            mpp[ord(s[r]) - ord('A')] += 1
            maxf = max(maxf, mpp[ord(s[r]) - ord('A')])
            if ((r-l+1) - maxf) > k:
                mpp[ord(s[l]) - ord('A')] -= 1
                maxf = 0
                l += 1
            if ((r-l+1) - maxf) <= k:
                maxl = max(maxl, r-l+1)

            r += 1
        return maxl
