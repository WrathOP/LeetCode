class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hm = collections.defaultdict(list)
        res = []
        for i , n in enumerate(groupSizes):
            hm[n].append(i)
            if len(hm[n])== n:
                res.append(hm[n])
                hm[n]= []
        
        return res