class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
        
        if not diff:
            return True
        
        if len(diff) == 2:
            i, j = diff
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        return False