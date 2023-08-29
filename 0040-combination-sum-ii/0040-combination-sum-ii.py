class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(comb,idx):
            s = sum(comb)
            if s== target and comb not in res:
                res.append(comb)
            if s< target:
                for i in range(idx,len(candidates)):
                    if i > idx and candidates[i] == candidates[i-1]:  
                        continue
                    backtrack(comb+[candidates[i]],i+1)
        backtrack([],0)
        return res