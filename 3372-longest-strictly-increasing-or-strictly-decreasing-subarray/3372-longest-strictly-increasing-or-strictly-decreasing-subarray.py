class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = 1  # Track current increasing and decreasing lengths
        il = dl = 1    # Track longest increasing and decreasing lengths

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                il += 1          # Increment increasing length
                inc = max(inc, il)  # Update longest increasing length
                dl = 1           # Reset decreasing length
            elif nums[i] > nums[i + 1]:
                dl += 1          # Increment decreasing length
                dec = max(dec, dl)  # Update longest decreasing length
                il = 1           # Reset increasing length
            else:
                il = dl = 1      # Reset both lengths if elements are equal

        return max(inc, dec)     # Return the maximum length found