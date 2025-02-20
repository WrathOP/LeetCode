class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def backtrack(s):
            if len(s) == len(nums[0]):
                if s not in nums:
                    return s
                return ""
            res = backtrack(s + "0")
            if res:
                return res
            return backtrack(s + "1")
        

        return backtrack("")
                