class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        refill=0
        numB=numBottles 
        while numBottles >= numExchange:
            refill = refill + (numBottles // numExchange )
            numBottles = (numBottles // numExchange ) + (numBottles % numExchange)

        res= numB + refill  
        return res 

        