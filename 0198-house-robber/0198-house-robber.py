class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(idx):
            if idx == 0 :
                return nums[0]
            if idx< 0:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            pick = nums[idx] + f(idx-2)
            notPick = f(idx-1)
            dp[idx] = max(pick,notPick)
            return dp[idx]
        
        n= len(nums)
        dp = [-1 for i in range(n)]
        print(nums,len(dp))
        return f(n-1)