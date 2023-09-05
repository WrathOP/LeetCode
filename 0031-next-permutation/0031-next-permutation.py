class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i,lowest):
            nums[i],nums[lowest]= nums[lowest],nums[i]
        k = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
               k = i
               break
        
        if k == -1:
            nums.sort()
            return
        
        l = -1
        for i in range(len(nums) - 1, k - 1, -1):
            if nums[k] < nums[i]:
                l = i
                break
        # print(k,l)
        swap(k,l)
        # print(nums)
        nums[k+1:] = sorted(nums[k+1:])
        # print(nums)
