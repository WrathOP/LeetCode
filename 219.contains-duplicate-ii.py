#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map= {}

        for i,n in enumerate(nums):
            if n in hash_map:
                if abs(hash_map[n] - i) <= k:
                    return True
                hash_map[n] = i
            else:
                hash_map[n] = i
        
        return False
        
# @lc code=end

