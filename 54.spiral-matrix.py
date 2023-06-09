#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=n-1
        top=0
        bottom=m-1
        list1 = []
        while left<=right and top<=bottom:
            for i in range(left,right+1,1):
                list1.append(matrix[top][i])
            top+=1
            
            for i in range(top,bottom+1,1):
                list1.append(matrix[i][right])
            right-=1
            if len(list1)==m*n:
                break
            for i in range(right,left-1,-1):
                list1.append(matrix[bottom][i])
            bottom-=1
            for i in range(bottom,top-1,-1):
                list1.append(matrix[i][left])
            left+=1
        return list1
# @lc code=end

