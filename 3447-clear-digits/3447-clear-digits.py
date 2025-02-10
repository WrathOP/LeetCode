class Solution:
    def clearDigits(self, s: str) -> str:
        mark = set() 
        for i,n in enumerate(s):
            # print("normal",n)
            if n.isdigit():
                # print("is digit",n)
                mark.add(i)
                while i >= 0:
                    # print(s[i].isdigit() , mark)
                    if not s[i].isdigit() and i not in mark:
                        mark.add(i)
                        break
                    i -= 1
        
        # print(mark)
        res = ""
        for i in range(len(s)):
            if i not in mark:
                res += s[i]
        return res
                
                
                        
                        
                        
                    
                
                
        