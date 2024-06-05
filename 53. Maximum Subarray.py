class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        s=0
        maxi=nums[0]
        for i in range(n):
            s+=nums[i]
            maxi=max(maxi,s)
            if s<0:
                s=0
        return maxi
