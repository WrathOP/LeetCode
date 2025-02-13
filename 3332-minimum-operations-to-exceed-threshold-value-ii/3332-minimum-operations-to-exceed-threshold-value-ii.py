class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        heapq.heapify(nums) 

        while len(nums)> 1 and  nums[0] < k:
            smol1 = heapq.heappop(nums)
            smol2 = heapq.heappop(nums)

            heapq.heappush(nums, (smol1 * 2)+ smol2)
            res += 1

        return res
            