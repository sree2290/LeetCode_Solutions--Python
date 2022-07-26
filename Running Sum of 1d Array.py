class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new = [0] * len(nums)
        new[0] = nums[0]
        for i in range(1,len(nums)):
            new[i] = new[i-1] + nums[i]
        return new
