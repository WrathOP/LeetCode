class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        maximum = 0
        l = bottom
        special.sort()
        for i ,value in enumerate(special):
            if i ==0:
                maximum = max(value-l,maximum)
                l = value
            else:
                maximum = max(value - l -1 , maximum)
                l = value
        maximum = max(top-l,maximum)
        
        return maximum