class Solution:
    def findColMax(self, matrix, n, m, col):
        ind = -1
        maxi = -1
        for i in range(n):
            if matrix[i][col] > maxi:
                maxi = matrix[i][col]
                ind = i
        return ind

    def findPeakGrid(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = m-1
        while low <= high:
            mid = (low + high)//2
            col = self.findColMax(matrix, n, m, mid)
            left = matrix[col][mid-1] if mid-1>=0 else -1
            right = matrix[col][mid+1] if mid+1<m else -1
            if left < matrix[col][mid] and right < matrix[col][mid]: return [col,mid]
            elif left > matrix[col][mid]: high = mid -1
            else: low = mid + 1
        return [-1,-1]
