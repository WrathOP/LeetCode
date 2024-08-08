class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        r, c = rStart, cStart
        res = []
        index = 0
        steps = 1
        mult = rows * cols

        while len(res) < mult:
            for myResume in range(2):
                dr, dc = directions[index]
                for _ in range(steps):
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                    r, c = r + dr, c + dc
                index = (index + 1) % 4
            steps += 1

        return res
