class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums)-x
        left = 0
        right = 0
        currsum = 0
        minoperations = float('inf')
        if target <0:
            return -1
        if target == 0:
            return n
        while right < n:
            currsum += nums[right]
            right+=1
            
            while currsum > target and left < n:
                currsum -= nums[left]
                left+=1
            if currsum == target:
                minoperations = min(minoperations , n- (right- left))

        return -1 if minoperations == float('inf') else minoperations