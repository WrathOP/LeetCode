class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(row, col):
            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or grid[row][col] == "0"
            ):
                return

            grid[row][col] = "0"
            for dr, dc in directions:
                dfs(row + dr, col + dc)
        
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == "1"):
                    islands+=1
                    dfs(r,c)
        
        return islands
                
