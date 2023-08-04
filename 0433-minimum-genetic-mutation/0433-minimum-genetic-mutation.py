class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankSet = set(bank)
        options = ['A','C','G','T']
        visited , q = set(),deque()
        visited.add(startGene)
        q.append(startGene)
        count = 0

        while q:
            size= len(q)
            for i in range(size):
                gene = q.popleft()
                if gene == endGene:
                    return count
                for j in range(8):
                    for option in options:
                        newGene = gene[:j]+option + gene[j+1:]
                        if newGene in bankSet and newGene not in visited:
                            visited.add(newGene)
                            q.append(newGene)
            count +=1

        return -1

            
