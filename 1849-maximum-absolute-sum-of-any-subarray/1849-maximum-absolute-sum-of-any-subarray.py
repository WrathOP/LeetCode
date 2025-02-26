class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res1, res  = 0, 0
        prefix = 0

        for n in nums:
            if prefix > 0:
                prefix += n
            else:
                prefix = n
            res = max(res,prefix)
        
        prefix = 0
        for n in nums:
            if prefix < 0:
                prefix += n
            else:
                prefix = n
            
            res1 = min(res1, prefix)
            
        return max(abs(res1), res)
            
                