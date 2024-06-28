class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10**9 +7

        s1, s2 = [], []
        nex = [0]*n
        pre = [0]*n

        for i in range(n):
            while s1 and arr[s1[-1]] >= arr[i]:
                s1.pop()
            pre[i] = s1[-1] if s1 else -1
            s1.append(i)

        for i in range(n-1,-1,-1):
            while s2 and arr[s2[-1]] > arr[i]:
                s2.pop()
            nex[i] = s2[-1] if s2 else n
            s2.append(i)

        ans = 0
        for i in range(n):
            left = i - pre[i]
            right = nex[i] - i
            ans = (ans + arr[i]*left*right) % MOD
        
        return ans
