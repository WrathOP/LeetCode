#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = dict()
        hashmap2 = dict()

        for i in range(len(s)):
            if (s[i] in hashmap and hashmap[s[i]]!= t[i]) or (t[i] in hashmap2 and hashmap2[t[i]]!= s[i]):
                return False
            else:
                hashmap[s[i]] = t[i]
                hashmap2[t[i]] = s[i]
        return True
        
# @lc code=end

