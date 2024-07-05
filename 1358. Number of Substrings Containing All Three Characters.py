#BRUTE FORCE
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for i in range(n):
            mpp = [0] * 3
            for j in range(i,n):
                mpp[ord(s[j]) - ord('a')] = 1
                if (mpp[0] + mpp[1] + mpp[2]) == 3:
                    cnt += (n-j)
                    break

        return cnt

#OPTIMAL APPROACH
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = [-1,-1,-1]
        n = len(s)
        cnt = 0
        for i in range(n):
            last[ord(s[i]) - ord('a')] = i
            if (last[0] != -1 and last[1] != -1 and last[2] != -1):
                cnt += (1 + min(last[0], last[1], last[2]))

        return cnt
