class Solution:
    def helper(self, nums: List[int]) -> int:
        n= len(nums)
        # dp = [-1 for _ in range(n)]
        prev = nums[0]
        prev2 = 0

        for idx in range(1,n):
            pick = nums[idx] 
            if idx>1:
                pick += prev2
            notPick = prev
            curr = max(pick,notPick)
            prev2 , prev = prev , curr
        
        return prev
    def rob(self, nums: List[int]) -> int:
        if len(nums)== 1:
            return nums[0]
        temp1 = nums[:-1]
        temp2 = nums[1:]

        ans1 = self.helper(temp1)
        ans2 = self.helper(temp2)
        return max(ans1,ans2)
        