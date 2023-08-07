class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        res = []
        n = len(nums)
        def backtrack(comb):
            nonlocal n
            if len(comb) == n:
                res.append(comb.copy())
                return

            for num in nums:
                if num not in comb:
                    comb.append(num)
                    backtrack(comb)
                    comb.pop()
        
        backtrack([])
        return res