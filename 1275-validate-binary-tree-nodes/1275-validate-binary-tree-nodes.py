class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        children = set(leftChild) | set(rightChild)
        root = -1
        for i in range(n):
            if i not in children:
                root = i
        
        if root == -1:
            return False

        seen = {root}
        queue = deque([root])

        while queue:
            node = queue.popleft()
            for child in [leftChild[node],rightChild[node]]:
                if child != -1:
                    if child in seen:
                        return False

                    queue.append(child)
                    seen.add(child)

        return len(seen) == n
