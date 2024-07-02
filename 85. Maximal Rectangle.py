class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        heights = [0] * m
        maxa = 0
        for i in range(n):
            for j in range(m):
                heights[j] = heights[j] + 1 if matrix[i][j]=='1' else 0
            stack = []
            for j in range(m+1):
                while stack and (j==m or heights[stack[-1]] >= heights[j]):
                    height = heights[stack.pop()]
                    width = j if not stack else j - stack[-1] -1
                    maxa = max(maxa, height*width)
                stack.append(j)

        return maxa
