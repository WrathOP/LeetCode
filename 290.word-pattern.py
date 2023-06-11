#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # Solution 1:
        # Time: O(n)
        # Space: O(n)

        s_arr = list(s.split())
        n = len(pattern) - 1
        hashmap = dict()
        hashmap1 = dict()
        if len(s_arr) != len(pattern):
            return False
        for i in range(len(s_arr)):
            if (
                s_arr[i] in hashmap
                and hashmap[s_arr[i]] != pattern[i % n]
                or pattern[i % n] in hashmap1
                and hashmap1[pattern[i % n]] != s_arr[i]
            ):
                return False
            else:
                hashmap[s_arr[i]] = pattern[i % n]
                hashmap1[pattern[i % n]] = s_arr[i]
        
        return True
    


        # s_arr = list(s.split())
        # n = len(pattern) - 1
        # hashmap = dict()
        # hashmap1 = dict()
        # for i in range(len(s_arr)):
        #     if (
        #         s_arr[i] in hashmap and s_arr[i] in hashmap[s_arr[i]] != pattern[i % n]
        #     ) or (pattern[i % n] in hashmap1 and hashmap1[pattern[i % n]] != s_arr[i]):
        #         # print(pattern[i%n],s_arr[i],hashmap)
        #         return False
        #     else:
        #         # print(i)
        #         hashmap[s_arr[i]] = pattern[i % n]
        #         hashmap1[pattern[i % n]] = s_arr[i]

        # return True


# @lc code=end
