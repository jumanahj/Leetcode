class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        vis=set()
        while n!=1 and n not in vis:
            vis.add(n)
            sumA=0
            while n>0:
                rem=n%10
                sumA=sumA+(rem*rem)
                n=n//10
            n=sumA
        return n==1 