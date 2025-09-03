class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n=int(sqrt(num))
        if n*n == num:
            return True 
        return False 
        