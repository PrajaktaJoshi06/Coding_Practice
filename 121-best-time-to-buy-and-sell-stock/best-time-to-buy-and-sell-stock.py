class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0

        while r<len(prices):
            diff = prices[r] - prices[l]
            if diff>0:
                profit = max(diff, profit)
                r += 1
            else: 
                l=r
                r+=1
        return profit