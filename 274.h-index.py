#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        h = 0
        for i,v in enumerate(citations):
            if v >= i+1:
                h = i+1
        return h

# @lc code=end

