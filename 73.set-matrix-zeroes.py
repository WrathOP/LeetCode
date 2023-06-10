#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        pos = []
    
        # find all zeros 
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    pos.append( (i,j) )
                    
        # change it
        for i, j in pos:
            for x in range(c):
                matrix[i][x] = 0
            for y in range(r):
                matrix[y][j] = 0
        
# @lc code=end

