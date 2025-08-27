class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0

        seg=s.split(" ")
        return len(seg)
        