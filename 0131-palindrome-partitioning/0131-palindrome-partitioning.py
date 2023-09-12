class Solution:
    def is_valid(self,s):
        return s == s[::-1]
    def partition(self, s: str) -> List[List[str]]:
        res= []
        part= []

        def backtrack(i):
            if i>= len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if self.is_valid(s[i:j+1]):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
        backtrack(0)
        return res
