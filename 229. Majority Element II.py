# METHOD-1 (HASHING)
# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(N)
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        hashh=defaultdict(int)
        for i in range(n):
            hashh[nums[i]]+=1
        for num in hashh:
            if hashh[num]>(n//3):
                ans.append(num)
        return ans

# METHOD-2 
# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(1)

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n= len(nums)
        cnt1, cnt2 = 0, 0
        ele1, ele2 = float('inf'), float('inf')
        for i in range(n):
            if (cnt1 == 0 and nums[i] != ele2):
                ele1 = nums[i]
                cnt1 += 1
            elif (cnt2 == 0 and nums[i] != ele1):
                ele2 = nums[i]
                cnt2 += 1
            elif (nums[i] == ele1): cnt1 += 1
            elif (nums[i] == ele2): cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1 
        
        ans = []
        cnt1, cnt2 = 0, 0
        for i in range(n):
            if nums[i] == ele1:
                cnt1 += 1
            if nums[i] == ele2:
                cnt2 += 1
        if cnt1 > (n//3): ans.append(ele1)
        if cnt2 > (n//3): ans.append(ele2)
        ans.sort()
        return ans
