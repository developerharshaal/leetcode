class Solution:
    def helper(self, ind, arr, ans, ds):
        ans.append(ds.copy())
        
        for i in range(ind, len(arr)):
            if i != ind and arr[i] == arr[i-1]: continue
            ds.append(arr[i])
            self.helper(i+1, arr, ans, ds)
            ds.pop()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        ds = []
        self.helper(0, nums, ans, ds)
        return ans
