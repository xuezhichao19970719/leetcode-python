class Solution:
    def maxProfit(self, prices):
        p = 0
        for i in range(len(prices)-1):
            a = prices[i+1] - prices[i]
            p +=  if prices[i] < prices[i+1] else 0
        return p
            