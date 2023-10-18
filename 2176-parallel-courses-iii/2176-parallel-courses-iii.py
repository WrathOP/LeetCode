class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        pregraph = {i:set([]) for i in range(1,n+1)}
        for s,e in relations:
            pregraph[e].add(s)
        
        @cache
        def dp(i):
            if not pregraph[i]:
                return time[i-1]
            else:
                return time[i-1] + max(dp(j) for j in pregraph[i])
            
        res = 0
        for i in range(1,n+1):
            res = max(res,dp(i))
        
        return res

