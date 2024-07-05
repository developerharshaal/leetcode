class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = sum(cardPoints[:k])
        n = len(cardPoints)
        maxSum = 0
        rsum = 0
        maxSum = lsum
        rind = n-1
        for i in range(k-1,-1,-1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rind]
            rind -= 1
            maxSum = max(maxSum, lsum + rsum)
        return maxSum
