class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        temp = ""
        for c in s:
            if c != " ":
                temp += c
            elif temp != "":
                if res != '':
                    res = temp + " "+ res
                else:
                    res = temp
                temp = ""
        if temp != "":
            if res != '':
                res = temp + " " + res
            else:
                res = temp
        return res

            
