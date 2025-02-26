class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix_sum = 0
        even = 0
        odd = 0
        MOD = 10**9 + 7
        res = 0

        for a in arr:
            prefix_sum += a
            
            if prefix_sum % 2:
                res = (res +1 + even) % MOD
                odd +=1 
            else:
                res = (res + odd ) % MOD
                even +=1 

        return res
