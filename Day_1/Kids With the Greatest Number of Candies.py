class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new = []
        high_candy = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= high_candy:
                new.append(True)
            else:
                new.append(False)
        return new
