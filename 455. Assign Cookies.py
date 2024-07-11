class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l, r = 0, 0
        n = len(g)
        m = len(s)
        while r < m and l < n:
            if s[r] >= g[l]:
                l += 1
            r += 1
        return l
