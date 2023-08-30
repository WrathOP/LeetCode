class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        totalsteps = 0
        left = nums[-1]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]> left:
                steps =(nums[i]-1)//left
                left = nums[i]//(steps+1)
                totalsteps += steps
                print("steps : ", steps )   
                print("left : ", left)
                print("total steps", totalsteps)
            else:
                left = nums[i]

        return totalsteps