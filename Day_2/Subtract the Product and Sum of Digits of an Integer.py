class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        prod = 1
        for i in str(n):
            prod = prod*int(i)
            summ = summ +int(i)
        return prod - summ
            
