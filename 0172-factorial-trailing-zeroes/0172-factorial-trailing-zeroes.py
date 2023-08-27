class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        power = 5
        while n//power != 0:
            n = n//power
            zeros += n
        
        return zeros
            