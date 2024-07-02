class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left = [-1] * n
        right = [n] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        area = 0
        for i in range(n):
            area = max(area, (right[i]-left[i]-1)*heights[i])

        return area





class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxa = 0
        for i in range(n+1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack[-1]]
                stack.pop()
                if not stack: width = i
                else : width = i - stack[-1] - 1
                maxa = max(maxa, height*width)

            stack.append(i)
        return maxa
