class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        if n == 0:
            return 0
        if n == 1:
            return max(energyDrinkA[0], energyDrinkB[0])
        
        maxA = [0] * n
        maxB = [0] * n
        
        maxA[0] = energyDrinkA[0]
        maxB[0] = energyDrinkB[0]
        
        maxA[1] = energyDrinkA[0] + energyDrinkA[1]
        maxB[1] = energyDrinkB[0] + energyDrinkB[1]
        
        for i in range(2, n):
            maxA[i] = max(energyDrinkA[i] + maxA[i-1], energyDrinkA[i] + maxB[i-2])
            maxB[i] = max(energyDrinkB[i] + maxB[i-1], energyDrinkB[i] + maxA[i-2])
        
        return max(maxA[-1], maxB[-1])
