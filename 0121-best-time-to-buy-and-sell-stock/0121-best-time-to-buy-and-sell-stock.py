class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        profit = 0
        n = len(prices)
        for r in range(n):
            if prices[r] < prices[l]:
                l = r
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        return max_profit