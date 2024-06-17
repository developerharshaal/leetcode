class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1 = []
        m2 = []
        for ind in s:
            m1.append(s.index(ind))
        for ind in t:
            m2.append(t.index(ind))
        print(m1,m2)
        if m1 == m2:
            return True
        return False
