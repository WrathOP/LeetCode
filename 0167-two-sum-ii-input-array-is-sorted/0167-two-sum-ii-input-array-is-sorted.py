class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i , n in enumerate(numbers):
            tar =  target - n
            print(tar)
            l = i
            r = len(numbers)
            # print(l,r)
            while l < r:
                mid = (l+r) >> 1
                print(mid, numbers[mid])
                if numbers[mid] > tar:
                    r = mid
                elif numbers[mid] < tar:
                    l = mid+1
                else:
                    return [i+1,mid+1]