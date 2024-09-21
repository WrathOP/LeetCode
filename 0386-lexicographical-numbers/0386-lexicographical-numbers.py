class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [] 

        def dfs(num):
            for i in range(10):
                temp = (num * 10) + i 
                if temp > n or temp < 1:
                    continue  
                res.append(temp)
                dfs(temp)
        

        dfs(0)
        return res
                