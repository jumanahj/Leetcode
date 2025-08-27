class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        step=0
        while n>=step+1:
            step=step+1
            n=n-step
        return step
            