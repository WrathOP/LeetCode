class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]):
        mod = 10**9+7
        arr.sort()
        n = len(arr)
        lookup = collections.defaultdict(int)
        for i in range(n):
            temp = 1
            for j in range(i-1,-1,-1):
                temp += (lookup[arr[j]]*lookup[arr[i]/arr[j]])
            lookup[arr[i]]= temp

        
        return sum(lookup.values())%mod
