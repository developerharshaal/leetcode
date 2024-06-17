from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ''
        hashh = Counter(s)
        sorted_dict = sorted(hashh.items(), key = lambda item: (-item[1], item[0]))
        for i in sorted_dict:
            ans += i[0]*i[1]
        return ans
