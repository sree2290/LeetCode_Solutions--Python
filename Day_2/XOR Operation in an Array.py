class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        total = 0
        for i in range(n):
            c = start + 2 * i
            total = total^c
            #print(c)
        #print(total)
        return total
