class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        element=None

        for i in range(len(nums)):
            if cnt==0:
                element=nums[i]
            if nums[i]==element:
                cnt+=1
            else:
                cnt-=1
        return element
