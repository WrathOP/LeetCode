#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return set(s) == set(t) and all(s.count(c) == t.count(c) for c in set(s))
        
# @lc code=end

