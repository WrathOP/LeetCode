# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findPeak(self,mountain_arr,right):
        left  = 0
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        
        return left
    
    def binarySearch(self,mountain_arr,target,left,right,is_upside):
        while left <= right:
                mid = (left + right)>> 1
                mid_val = mountain_arr.get(mid)
                if mid_val == target:
                    return mid 
                if is_upside:
                    if target > mid_val:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if target > mid_val:
                        right = mid - 1
                    else:
                        left = mid + 1
        return -1

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()-1
        peak = self.findPeak(mountain_arr,length)
        leftPortion = self.binarySearch(mountain_arr,target,0,peak,True)
        if leftPortion != -1:
            return leftPortion
        rightPortion = self.binarySearch(mountain_arr,target,peak+1,length,False)
        return rightPortion
        