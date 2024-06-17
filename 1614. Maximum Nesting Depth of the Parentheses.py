class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        cnt = 0
        for i in s:
            if i == '(':
                cnt += 1
            elif i == ')':
                cnt -= 1
            maxi = max(maxi, cnt)
        return maxi
