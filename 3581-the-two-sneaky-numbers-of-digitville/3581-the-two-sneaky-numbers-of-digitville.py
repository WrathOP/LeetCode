class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        visited = [] 
        res = []

        for num in nums:
            if len(res)== 2: return res
            if num in visited:
                res.append(num)
            else:
                visited.append(num)
        return res