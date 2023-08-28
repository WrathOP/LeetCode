class Solution:
    def solve(self,n,dp):
        if n <=2:
            return n
        if dp[n]!= -1:
            return dp[n]
        
        left = self.solve(n-1,dp)
        right =self.solve(n-2,dp)
            
        dp[n] = left + right
        return dp[n]
    
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp = [-1]* (n+1)

        return self.solve(n,dp)