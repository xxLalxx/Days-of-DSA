# Q)You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        best_profit=0
        for i in range (0,len(prices)):
            for j in range(i+1,len(prices)):
                profit= j-i
                if(best_profit<profit):
                    best_profit=profit
        if(best_profit<=0):
            return("no profitable days seen")
        else:
            return(best_profit)