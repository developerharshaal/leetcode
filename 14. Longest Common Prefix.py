class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        size = min(len(first), len(last))
        for i in range(size):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans
