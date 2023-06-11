#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = dict()
        for c in magazine:
            if c in hashmap:
                hashmap[c] += 1
            else:
                hashmap[c] = 1
        for c in ransomNote:
            if c not in hashmap:
                return False
            elif hashmap[c] == 0:
                return False
            else:
                hashmap[c] -= 1
        return True
# @lc code=end

