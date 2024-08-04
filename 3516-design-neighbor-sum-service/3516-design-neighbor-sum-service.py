class neighborSum:
    grid = []

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def getAdj(self, i: int , j: int):
        adj_sum = 0
        row , col = len(self.grid), len(self.grid[0])
        if i + 1 < row :
            adj_sum += self.grid[i+1][j]
        if i -1 >= 0 :
            adj_sum += self.grid[i-1][j]
        if j + 1 < col :
            adj_sum += self.grid[i][j+1]
        if j - 1 >= 0 :
            adj_sum += self.grid[i][j-1]
        return adj_sum
        
    def adjacentSum(self, value: int) -> int:
        for i,row in enumerate(self.grid):
            for j, col in enumerate(row):
                if col == value:
                    return self.getAdj(i,j)

    def getDiag(self, i: int, j: int):
        diag_sum = 0
        row, col = len(self.grid), len(self.grid[0])
        if i - 1 >= 0 and j - 1 >= 0:
            diag_sum += self.grid[i - 1][j - 1]
        if i + 1 < row and j + 1 < col:
            diag_sum += self.grid[i + 1][j + 1]
        if i - 1 >= 0 and j + 1 < col:
            diag_sum += self.grid[i - 1][j + 1]
        if i + 1 < row and j - 1 >= 0:
            diag_sum += self.grid[i + 1][j - 1]
        return diag_sum

    def diagonalSum(self, value: int) -> int:
        for i, row in enumerate(self.grid):
            for j,col in enumerate(row):
                if col == value:
                    return self.getDiag(i, j)


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
