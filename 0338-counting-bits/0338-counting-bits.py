class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [i for i in range(n+1)]
        for i in range(n+1):
            res[i] = res[i//2]+i%2
        
        return res