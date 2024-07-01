class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        mins, maxs = 0, 0

        stack = []
        for nex in range(n+1):
            while stack and (nex == n or nums[stack[-1]] > nums[nex]):
                i = stack.pop()
                prev = stack[-1] if stack else -1
                mins += nums[i] * (nex - i) * (i - prev)
            stack.append(nex)

        stack = []
        for nex in range(n+1):
            while stack and (nex == n or nums[stack[-1]] < nums[nex]):
                i = stack.pop()
                prev = stack[-1] if stack else -1
                maxs += nums[i] * (nex - i) * (i - prev)
            stack.append(nex)

        return maxs - mins
