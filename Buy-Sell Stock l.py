class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l,r = 0,1      #LEFT AND RIGHT POINTER FOR A DAY AND SUCCEEDING DAY
        Max_Profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:       # IF THE NEXT DAY PRICE IS GREATER....CALCULATE PROFIT
                Profit = prices[r] - prices[l] 
                Max_Profit = max(Max_Profit,Profit)
            else:                             # IF THE NEXT DAY PRICE HAS DROPPED...INCREMENT THE RIGHT POINTER ONLY 
                l = r
            r += 1

        return Max_Profit