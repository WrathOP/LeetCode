class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)] 
        self.rank = [1] * (n+1)
        self.size = [1] * (n+1) 

    def getUltParent(self, n):
        if self.parent[n] == n:
            return n
        # Path compression
        self.parent[n] = self.getUltParent(self.parent[n])
        return self.parent[n]
    
    def unionByRank(self, n1, n2):
        ultParent1 = self.getUltParent(n1)
        ultParent2 = self.getUltParent(n2)
        
        if ultParent1 == ultParent2:
            return
        
        if self.rank[ultParent1] > self.rank[ultParent2]:
            self.parent[ultParent2] = ultParent1
        elif self.rank[ultParent1] < self.rank[ultParent2]:
            self.parent[ultParent1] = ultParent2
        else:
            self.parent[ultParent2] = ultParent1
            self.rank[ultParent1] += 1

    def unionBySize(self,n1,n2):
        ultParent1 = self.getUltParent(n1)
        ultParent2 = self.getUltParent(n2)
        
        if ultParent1 == ultParent2:
            return
        
        if self.size[ultParent1] > self.size[ultParent2]:
            self.parent[ultParent2]= ultParent1
            self.size[ultParent1]+= self.size[ultParent2]
        else:
            self.parent[ultParent1]= ultParent2
            self.size[ultParent2]+= self.size[ultParent1]
    
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row = max(x for x, y in stones)
        col = max(y for x, y in stones)
        ds = DisjointSet(row+col+1)
        
        existStones = set()
        for stone in stones:
            ds.unionBySize(stone[0],stone[1] + row + 1)
            existStones.add(stone[0])
            existStones.add(stone[1] + row + 1)
        
        count= 0
        for i in existStones:
            if ds.getUltParent(i) == i:
                count+=1
                
        return len(stones) - count

            
            
            
            
        