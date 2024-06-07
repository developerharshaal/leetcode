# BRUTE FORCE
# TIME COMPLEXITY: O(N^3)
# SPACE COMPLEXITY: O(N)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        st = set()
        hash={}
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        st.add(tuple(temp))
        ans = [list(s) for s in st]
        return ans


# BETTER APPROACH
# TIME COMPLEXITY: O(N^2)
# SPACE COMPLEXITY: O(N)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        st = set()
        for i in range(n):
            arr = []
            for j in range(i+1,n):
                temp = []
                k = -(nums[i] + nums[j])
                if k in arr:
                    temp = [nums[i], nums[j], k]
                    temp.sort()
                    st.add(tuple(temp))
                arr.append(nums[j])
        ans = [list(s) for s in st]
        return ans


# OPTIMAL APPROACH (USING POINTERS)
# TIME COMPLEXITY: O(N^2)
# SPACE COMPLEXITY: O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n):
            if i != 0 and nums[i]==nums[i-1]: continue
            j = i+1
            k = n-1
            while (j < k):
                summ = nums[i] + nums[j] + nums[k]
                if summ > 0:
                    k -= 1
                elif summ < 0:
                    j += 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    while (j < k and nums[j] == nums[j-1]): j += 1
                    while (j < k and nums[k] == nums[k+1]): k -= 1
        return ans
