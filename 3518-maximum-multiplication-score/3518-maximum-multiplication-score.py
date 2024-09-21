from typing import List

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        dp = [[-float('inf')] * 5 for _ in range(n + 1)]
        
        for j in range(n + 1):
            dp[j][0] = 0
        
        for j in range(1, n + 1):
            for i in range(1, min(5, j + 1)):
                dp[j][i] = dp[j-1][i]
                
                dp[j][i] = max(dp[j][i], dp[j-1][i-1] + a[i-1] * b[j-1])
        
        return dp[n][4]