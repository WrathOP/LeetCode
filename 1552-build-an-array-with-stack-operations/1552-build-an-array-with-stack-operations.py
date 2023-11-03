class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        test = []
        idx = 0
        for i in range(1,n+1):
            if test == target:
                return stack
            if i == target[idx]:
                stack.append('Push')
                test.append(i)
                idx+=1 if idx+1 < len(target) else 0
            else:
                stack.append('Push')
                stack.append('Pop')
            # print(stack,idx)
        
        return stack