#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i,n in enumerate(nums):
            if target - n in hash_table:
                return [hash_table[target-n], i]
            hash_table[n] = i
        return []
        
# @lc code=end

