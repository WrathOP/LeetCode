# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        total = 0
        def rec(node):
            nonlocal total
            if node is None:
                return 0,0
                
            leftsum,left = rec(node.left)
            rightsum ,right = rec(node.right)

            currsum = node.val + leftsum + rightsum
            currcount = 1+ left+right

            if currsum // currcount == node.val:
                total+=1
            
            return currsum,currcount

        rec(root)
        return total




        rec(root,total,currTotal,n)
        return total