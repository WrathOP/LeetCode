# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
        
        values = []
        dfs(root)
        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []

        for num in values:
            if num == curr_num:
                curr_streak+=1
            else:
                curr_streak = 1
                curr_num = num
            
            if curr_streak > max_streak:
                ans = []
                max_streak = curr_streak
            if curr_streak == max_streak:
                ans.append(num)
        return ans