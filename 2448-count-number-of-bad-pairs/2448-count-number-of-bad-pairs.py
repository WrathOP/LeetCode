class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        pairs = defaultdict(int)
        good = 0
        total = 0
        for i, n in enumerate(nums):
            total += i
            good += pairs[i-nums[i]]
            pairs[i-nums[i]] += 1
        
        return total - good


        