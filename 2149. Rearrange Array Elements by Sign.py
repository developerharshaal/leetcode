# BRUTE FORCE
# TIME COMPLEXITY: O(n)
# SPACE COMEPLEXITY: O(n)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos=[]
        neg=[]
        for i in range(n):
            if nums[i]>=0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        
        for i in range(len(pos)):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i]
        return nums


# OPTIMAL
# TIME COMPLEXITY: O(n)
# SPACE COMEPLEXITY: O(n)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        pos=0
        neg=1
        for num in nums:
            if num>0:
                ans[pos]=num
                pos+=2
            else:
                ans[neg]=num
                neg+=2
        return ans
