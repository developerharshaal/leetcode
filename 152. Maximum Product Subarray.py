# BRUTE FORCE
# TIME COMPLEXITY: O(N^2)
# SPACE COMPLECITY: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxPro = nums[0]
        for i in range(n):
            pro = nums[i]
            for j in range(i+1,n):
                maxPro = max(maxPro, pro)
                pro *= nums[j]
            maxPro = max(maxPro, pro)
        return maxPro
    
# OPTIMAL APPROACH
# TIME COMPLEXITY: O(N)
# SPACE COMPLECITY: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = -float('inf')
        pre, suf = 1, 1
        for i in range(n):
            if pre == 0: pre = 1
            if suf == 0: suf = 1
            pre = pre * nums[i]
            suf = suf * nums[n-i-1]
            maxi = max(maxi ,max(pre, suf))
        return maxi
