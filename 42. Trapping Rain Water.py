class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        cnt = 0
        for i in range(n):
            j = i
            l = 0
            r = 0
            while j >= 0:
                l = max(l, height[j])
                j -= 1
            j = i
            while j < n:
                r = max(r, height[j])
                j += 1
            cnt += min(r,l) - height[i]

        return cnt

        
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre = [0] * n
        post = [0] * n
        pre[0] = height[0]
        for i in range(1,n):
            pre[i] = max(height[i], pre[i-1])
        post[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            post[i] = max(height[i], post[i+1])
        
        cnt = 0
        for i in range(n):
            cnt += min(pre[i],post[i]) - height[i]
        return cnt



class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        res = 0
        right, left = 0, 0
        while l <= r:
            if height[l] <= height[r]:
                if height[l] >= left: left = height[l]
                else: res += left - height[l]
                l += 1
            else:
                if height[r] >= right: right = height[r]
                else: res += right - height[r]
                r -= 1
        return res
