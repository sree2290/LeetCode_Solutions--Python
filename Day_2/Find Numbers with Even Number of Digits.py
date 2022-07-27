class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        eve = 0
        for i in nums:
            if len(str(i))%2 == 0:
                eve = eve+1
            else:
                pass
        return eve
        
