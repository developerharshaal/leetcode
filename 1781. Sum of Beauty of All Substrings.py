from collections import defaultdict

class Solution:
    def beauty(self, freq):
        if not freq:
            return 0
        min_freq = min(freq.values())
        max_freq = max(freq.values())
        return max_freq - min_freq

    def beautySum(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            freq = defaultdict(int)
            for j in range(i, n):
                freq[s[j]] += 1
                res += self.beauty(freq)
        return res
