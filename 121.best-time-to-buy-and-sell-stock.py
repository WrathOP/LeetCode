#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for price in prices:
            lowest = min(price,lowest)
            profit = max(profit,price-lowest)
        return profit
# @lc code=end

