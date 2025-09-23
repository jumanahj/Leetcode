class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        pois=0
        for i in range(len(timeSeries)-1):
            pois+=min(timeSeries[i+1]-timeSeries[i],duration)
        return pois+duration
        