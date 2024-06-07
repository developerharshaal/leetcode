# BETTER METHOD
# TIME COMPLEXITY: O(N^3)
# SPACE COMPLEXITY: O(N)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        st = set()
        for i in range(n):
            for j in range(i+1,n):
                arr = []
                for k in range(j+1,n):
                    fourth = target - (nums[i] + nums[j] + nums[k])
                    if fourth in arr:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        st.add(tuple(temp))
                    arr.append(nums[k])
        ans=[list(x) for x in st]
        return ans


# OPTIMAL APPROACH
# TIME COMPLEXITY: O(N^3)
# SPACE COMPLEXITY: O(1)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1,n):
                if j != i+1 and nums[j] == nums[j-1]: continue
                k = j+1
                l= n-1
                while k<l:
                    summ = nums[i] + nums[j] + nums[k] + nums[l]
                    if summ == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        ans.append(temp)
                        k += 1
                        l -= 1
                        while (k < l and nums[k] == nums[k-1]): k += 1
                        while (k < l and nums[l] == nums[l+1]): l -= 1
                    elif summ > target: l -= 1
                    else: k += 1
        return ans

