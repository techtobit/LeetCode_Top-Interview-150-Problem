class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit =0
        l=0
        r= 1
        # mehtod - "Two Pointer"
        # while r < len(prices):
        #     if prices[r] > prices[l]:
        #         profit = prices[r]-prices[l]
        #         maxProfit = max(maxProfit, profit)
        #     else:
        #         l=r
        #     r +=1

        # mehtod - "Single Pass Approach"
        # By Tracking 
        minCost = prices[0]
        # while r<len(prices):
        #     if minCost > prices[l]:
        #         minCost = prices[l]
        #     res = prices[l]-minCost
        #     if maxProfit < res:
        #         maxProfit = res
        #     r +=1
        #     l +=1


        #  by for loop
        for num in prices:
            minCost = min(num, minCost)
            profit = num-minCost
            maxProfit = max(maxProfit, profit)

        return  maxProfit