from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        candidate = -1
        votes = 0
        
        # Boyer-Moore Voting 
        for num in nums:
            if votes == 0:
                candidate = num
                votes = 1
            elif num == candidate:
                votes += 1
            else:
                votes -= 1
        
        total_count = nums.count(candidate)
        if total_count * 2 <= len(nums):
            return -1  
        
        left_count = 0
        for i in range(len(nums) - 1):  
            if nums[i] == candidate:
                left_count += 1
            
            left_size = i + 1
            right_size = len(nums) - left_size
            right_count = total_count - left_count
            
            if left_count * 2 > left_size and right_count * 2 > right_size:
                return i
        
        return -1
