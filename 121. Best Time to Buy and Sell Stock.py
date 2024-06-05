class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxPro=0
        minP=9999999
        for i in range(n):
            minP=min(minP,prices[i])
            maxPro=max(maxPro,prices[i]-minP)
        return maxPro
