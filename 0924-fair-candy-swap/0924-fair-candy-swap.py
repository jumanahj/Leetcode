class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sum_a=sum(aliceSizes)
        sum_b=sum(bobSizes)
        form =(sum_b-sum_a)//2

        setB= set(bobSizes)
        for x in aliceSizes:
            y= x+form
            if y in setB:
                return[x,y]
        