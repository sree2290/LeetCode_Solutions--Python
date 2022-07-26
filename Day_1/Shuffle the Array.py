class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first = nums[n:]
        second = nums[:n]
        new_lis = []
        for i,j in zip(first,second):
            new_lis.append(j)
            new_lis.append(i)

        return new_lis
