class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start,comb):
            s = sum(comb)
            if s == target:
                res.append(comb.copy())
            elif s< target:
                for i in range(start,len(candidates)):
                    backtrack(i,comb+[candidates[i]])
        

        backtrack(0,[])
        return res