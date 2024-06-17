class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0]) if n >0 else 0
        low = 0
        high = n*m - 1
        while low <= high:
            mid = (low + high)//2
            i = mid // m
            j = mid % m
            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: high = mid - 1
            else: low = mid + 1
        return False
