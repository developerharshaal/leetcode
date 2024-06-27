class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nex = {}
        st = []

        for ele in reversed(nums2):
            while st and st[-1] <= ele:
                st.pop()

            if st:
                nex[ele] = st[-1]
            else:
                nex[ele] = -1

            st.append(ele)

        return [nex[el] for el in nums1]