class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        directions = {"UP": [-1, 0], "DOWN": [1, 0], "RIGHT": [0, 1], "LEFT": [0, -1]}

        current = [0, 0]

        grid = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append((i * n) + j)
            grid.append(row)

        for command in commands:
            dr, dc = directions[command]
            current = [current[0] + dr, current[1] + dc]

        return grid[current[0]][current[1]]
