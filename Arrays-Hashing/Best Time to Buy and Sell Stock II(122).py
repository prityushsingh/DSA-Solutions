class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        start = prices[0]
        len1 = len(prices)
        for i in range(0 , len1):
            if start < prices[i]: 
                profit += prices[i] - start
            start = prices[i]
        return profit


#Time complexity : O(N)
#Space complexity : O(1)
