# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.hashset = set()
        q = deque([(root, 0)])
        
        while q:
            for _ in range(len(q)):
                node, value = q.popleft()
                print(value)
                if node.left:
                    q.append((node.left,2*value + 1))
                    self.hashset.add(2*value + 1)
                if node.right:
                    q.append((node.right, 2*value + 2))
                    self.hashset.add(2*value + 2)
        

    def find(self, target: int) -> bool:
        return target in self.hashset
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)