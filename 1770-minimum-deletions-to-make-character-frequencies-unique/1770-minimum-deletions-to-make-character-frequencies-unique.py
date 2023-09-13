class Solution:
    def minDeletions(self, s: str) -> int:
        hm = collections.defaultdict(int)
        freqset = set()
        deletions = 0
        for c in s :
          hm[c]+=1
        
        for freq in hm.values():
          while freq > 0 and freq in freqset:
            freq-=1
            deletions +=1
          freqset.add(freq)

        return deletions 