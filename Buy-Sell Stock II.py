class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        Profit = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i - 1]:        #IF THE NEXT DAY THE PRICE HAS BECOME HIGHER ADD THAT TO PROFIT 
                Profit += prices[i] - prices[i - 1]
        
        return Profit
