# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List


def maxProfit(prices: List[int]) -> int:
    res = 0
    lowest = prices[0]

    for price in prices:
        if price < lowest:
            lowest = price
        res = max(res, price - lowest)

    return res


prices = [7, 1, 5, 3, 6, 4]
maxProfit(prices)
