#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r = len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]>target:
                r-=1
            elif numbers[l]+numbers[r]<target:
                l+=1
            else:
                if l!=r:
                    return [l+1,r+1]
                else:
                    l+=1
# @lc code=end

