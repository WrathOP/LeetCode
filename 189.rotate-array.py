#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    

    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums,l,r):
            while l<r:
                nums[l],nums[r]= nums[r],nums[l]
                l+=1
                r-=1
        
        k %= len(nums)
        nums.reverse()
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)
        
# @lc code=end

