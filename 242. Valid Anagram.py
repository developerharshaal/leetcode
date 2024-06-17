from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashh = defaultdict(int)
        for i in s:
            hashh[i] += 1
        for j in t:
            if j in hashh:
                hashh[j]-=1
            else:
                return False
        for i in hashh:
            if hashh[i] != 0:
                return False
        return True
