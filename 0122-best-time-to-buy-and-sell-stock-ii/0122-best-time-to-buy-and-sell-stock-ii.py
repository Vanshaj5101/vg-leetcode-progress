class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        for p in prices:
            if p < buy_price:
                buy_price = p
            else:
                profit += p-buy_price
                buy_price = p
        return profit