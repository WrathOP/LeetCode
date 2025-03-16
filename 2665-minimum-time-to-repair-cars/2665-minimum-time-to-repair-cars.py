class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l , r = 1, ranks[0] * cars * cars
        res = -1
        
        def isGood(min):
            car = 0
            for n in ranks:
                car += int(math.sqrt(min/n))
            return car >= cars
            
        while l <= r:
            mid = (l + r) >> 1
            if isGood(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1 
        return res
            
            
            
        