class Solution:
    def helper(self, ind, target, ds, arr, ans):
        n = len(arr)
        if ind == n:
            if target == 0: ans.append(ds.copy())
            return

        if arr[ind] <= target:
            ds.append(arr[ind])
            self.helper(ind, target-arr[ind],ds,arr,ans)
            ds.pop()

        self.helper(ind+1, target, ds,arr,ans)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ds =[]
        ans = []
        self.helper(0, target, ds, candidates,ans)
        return ans
