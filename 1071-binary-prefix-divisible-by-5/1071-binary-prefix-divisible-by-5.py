class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        sum = 0
        res=[]
        for i,n in enumerate(nums):
            sum = sum*2 + n
            if sum%5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res