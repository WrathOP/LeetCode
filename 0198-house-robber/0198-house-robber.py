class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        dp = [-1 for _ in range(n)]
        dp[0] = nums[0]
        
        for idx in range(1,n):
            pick = nums[idx] 
            if idx>1:
                pick += dp[idx-2]
            notPick = dp[idx-1]
            dp[idx] = max(pick,notPick)
        
        return dp[n-1]
        
        