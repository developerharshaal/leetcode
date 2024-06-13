# BRUTE FORCE
# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(1)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(len(arr)):
            if arr[i] <= k: k+=1
            else: break
        return k
    
# OPTIMAL APPROACH (BINARY SEARCH)
# TIME COMPLEXITY: O(LOG N)
# SPACE COMPLEXITY: O(1)

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n= len(arr)
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high)//2
            missing = arr[mid] - (mid + 1)
            if missing < k : low = mid + 1
            else: high = mid - 1
        return k + high + 1
    
