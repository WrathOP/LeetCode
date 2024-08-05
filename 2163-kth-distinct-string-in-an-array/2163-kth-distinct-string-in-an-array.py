class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        print(c)
        for key in c.keys():
            if c[key] == 1:
                k -= 1
                if k == 0:
                    return key

        return ""
