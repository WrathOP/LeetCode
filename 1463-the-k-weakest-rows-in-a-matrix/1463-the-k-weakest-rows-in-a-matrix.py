class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rs = [[sum(row),i] for i,row in enumerate(mat)]
        rs.sort()
        return [row[1] for row in rs[:k]]