class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(idx,comb):
            if idx >= n:
                res.append(comb)
                return
            backtrack(idx+1,comb)
            backtrack(idx+1,comb+[nums[idx]])
        
        backtrack(0,[])
        return res