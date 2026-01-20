class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        for i in range(1<<n):
            g = i ^ (i>>1)
            res.append(g)
        return res

        