class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operations = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "*": lambda x,y: x*y
        }

        left, right = 0, len(expression) - 1
        
        def backtrack(left,right):
            res = []

            for i in range(left, right+1):
                if expression[i] in operations:
                    res1 = backtrack(left,i-1)
                    res2 = backtrack(i+1,right)
                
                    for n in res1:
                        for n2 in res2:
                            res.append(operations[expression[i]](n,n2))
            
            if res ==[]:
                res.append(int(expression[left:right+1]))

            return res

        return backtrack(left,right)
                        
                    