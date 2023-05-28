#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ms = set()
        i  = 0
        while i < len(nums):
            if nums[i] in ms:
                nums.pop(i)
            else:
                ms.add(nums[i])
                i+=1
        return len(ms)
        
# @lc code=end

