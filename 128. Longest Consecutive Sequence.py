# METHOD-1 (MAKING SET)
# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(N)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        st=0
        cur_st=0
        for num in nums:
            if num-1 not in nums:
                cur=num
                cur_st=1

                while cur+1 in nums:
                    cur+=1
                    cur_st+=1
            st=max(st,cur_st)
        return st


# METHOD-2 (SORTING)
# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(N)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        cnt = 0
        ls = 1
        lastsmall = -float('inf')
        if n==0:
            return 0
        for i in range(n):
            if nums[i]-1 == lastsmall:
                cnt += 1
                lastsmall = nums[i]
            elif lastsmall != nums[i]:
               cnt = 1
               lastsmall = nums[i]
            ls = max(ls, cnt)
        return ls 

#
