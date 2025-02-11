class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(part)
        for c in s:
            stack.append(c)

            if len(stack) >= n:
                if "".join(stack[-n:]) == part:
                    for _ in range(n):
                        # print(stack)
                        stack.pop()
        return "".join(stack)
