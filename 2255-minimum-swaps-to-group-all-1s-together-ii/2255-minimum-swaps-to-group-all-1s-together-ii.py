class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        #sliding window problem
        #append the nums to take out the circular issue
        ones= 0
        cir_nums = nums + nums 
        for num in nums:
            if num == 1:
                ones+=1
        
        l, r = 0, ones

        min_swap = len(nums)

        curr_swap = 0
        for num in cir_nums[l:r]:
            if num == 0:
                curr_swap +=1
        
        while r < len(cir_nums):
            curr_swap -= cir_nums[l] ^ 1
            if r < len(cir_nums):
                curr_swap += cir_nums[r] ^ 1
            min_swap = min(min_swap,curr_swap)
            l+=1
            r+=1
            
        return min_swap
            