class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = nums[0]
        for num in nums:
            if candidate == num:
                count +=1
            else:
                if count> 0:
                    count-=1
                else:
                    candidate = num
        return candidate
    