"""
profit = 4
              l
prices = [7,1,5,3,6,4]
              r
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit += prices[r] - prices[l]
                l += 1
            else:
                l = r

        return profit
        
            
        



