#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        if sum(diff)<0:
            return -1
        start = 0
        total = 0
        for i in range(len(diff)):
            total += diff[i]
            if total < 0:
                total = 0
                start = i + 1
        return start

# @lc code=end

