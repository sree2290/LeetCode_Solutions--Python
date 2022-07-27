class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        coun = 0
        val={}
        for i in nums:
            if i not in val:
                val[i]=0
            val[i]+=1

        for j in val:
            n=val[j]
            coun = coun +(n*(n-1)//2)

        return coun

                
