class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max = float("-inf")
        sum = 0
        for num in nums:
            sum = sum + num
            if sum>max:
                max = sum
            if sum < 0:
                sum = 0

        return max
        