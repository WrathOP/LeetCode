#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i,interval in enumerate(intervals):
            if interval[1] < newInterval[0] and intervals[i+1][0]> newInterval[1]:
                intervals.insert(i,newInterval) 
                return intervals          
            elif interval[1] < newInterval[0] and intervals[i+1] < newInterval[1]:
                j = 0
                while 
# @lc code=end

