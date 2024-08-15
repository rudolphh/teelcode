class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_p = float("inf")
        max_p = 0

        max_profit = 0

        for price in prices:
            min_p = min(min_p, price)

            if min_p == price:
                max_p = 0
            elif price > max_p:
                max_p = price

            max_profit = max(max_profit, max_p - min_p)

        return max_profit