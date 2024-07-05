#BRUTE APPROACH
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n):
            mpp = defaultdict(int)
            for j in range(i,n):
                mpp[nums[j]] += 1
                if len(mpp) == k: cnt += 1
                elif len(mpp) > k: break
        return cnt


#OPTIMAL APPROACH
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            n = len(nums)
            cnt = 0
            mpp = defaultdict(int)
            r, l = 0, 0
            while r < n:
                mpp[nums[r]] += 1
                while len(mpp) > k:
                    mpp[nums[l]] -= 1
                    if mpp[nums[l]] == 0: del mpp[nums[l]]
                    l += 1
                cnt += (r-l+1)            
                r += 1
            return cnt
        
        return helper(nums,k) - helper(nums,k-1)
