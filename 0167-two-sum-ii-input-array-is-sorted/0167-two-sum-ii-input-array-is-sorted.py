class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i , j = 0 , len(numbers)-1
        res = None

        while res != target:
            res = numbers[i] + numbers[j]

            if res > target:
                j -= 1
            else:
                i +=1  
        
        return [i,j+1]
                
                