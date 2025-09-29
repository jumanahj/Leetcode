class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        n=len(gain)
        alt=[0]*(n+1)
        alt[0]=0
        for i in range(1,n+1):
            alt[i]=alt[i-1]+gain[i-1]
        return max(alt)
        