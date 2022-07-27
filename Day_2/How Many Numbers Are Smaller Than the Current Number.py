class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        m = []
        for i in nums:
            x = 0
            for j in nums:
                if i>j:
                    x = x+1
                else:
                    pass
            m.append(x)
        return m
