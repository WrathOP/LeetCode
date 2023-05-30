#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        profit = 0
        for r in range(1,len(prices)):
            if prices[r]>prices[l]:
                profit+= prices[r]-prices[l]
                l+=1
            else:
                l+=1
        return profit

# @lc code=end

