class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, opened = [], 0
        for r in s:
            if r == '(' and opened > 0: res.append(r)
            if r == ')' and opened > 1: res.append(r)
            opened += 1 if r == '(' else -1
        return "".join(res)
