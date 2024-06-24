class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sub = 1 << n
        ans = []
        for num in range(sub-1):
            l = []
            for i in range(n-1):
                if (num & (i<<1)):
                    l.append(nums[i])
            ans.append(l)

        return ans
