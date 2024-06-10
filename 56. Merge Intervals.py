# BRUTE FORCE
# TIME COMPLEXITY: O{N LOG N)
# SPACE COMPLEXITY: O(N)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        ans = []
        intervals.sort()
        for i in range(n):
            start, end = intervals[i][0], intervals[i][1]
            if len(ans)!=0 and end <= ans[-1][1]:
                continue
            for j in range(i+1,n):
                if intervals[j][0] <= end:
                    end = max(end, intervals[j][1])
                else:
                    break
            ans.append([start,end])
        return ans

# OPTIMAL APPROACH
# TIME COMPLEXITY: O{N LOG N)
# SPACE COMPLEXITY: O(N)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        ans = []
        intervals.sort()
        for i in range(n):
            if len(ans) == 0 or ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
        return ans
