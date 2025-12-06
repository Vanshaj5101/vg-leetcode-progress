class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        for p in prices:
            buy_price = min(p, buy_price)
            profit = max(profit, p-buy_price)
        return profit
