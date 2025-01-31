# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    # Map to store serialized subtrees and their count
        subtrees = {}
        # List to store roots of duplicate subtrees
        result = []
        
        def dfs(node):
            if not node:
                return "#"  
            
            serialized = (f"{node.val},{dfs(node.left)},{dfs(node.right)}")
            
            if serialized in subtrees:
                subtrees[serialized][1] += 1
                if subtrees[serialized][1] == 2:
                    result.append(subtrees[serialized][0])
            else:
                subtrees[serialized] = [node, 1]  
                
            return serialized
        
        dfs(root)
        return result