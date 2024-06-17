class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        prevAns = 0
        for c in reversed(s):
            value = val[c]
            if value < prevAns:
                total -= value
            else:
                total += value
            prevAns = value
        return total
