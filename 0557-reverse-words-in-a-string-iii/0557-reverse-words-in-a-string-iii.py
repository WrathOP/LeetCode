class Solution:
    def reverseWords(self, s: str) -> str:
        ListString = s.split()
        res = []
        for word in ListString:
            res.append(word[::-1])
        
        return " ".join(res)