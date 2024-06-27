class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        st = []
        n = len(nums)
        for i in range(2*n-1,-1,-1):
            idx = i % n
            while st and st[-1] <= nums[idx]:
                st.pop()
            ans[idx] = st[-1] if st else -1
            st.append(nums[idx])

        return ans



