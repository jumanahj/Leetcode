class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word=s.split()
        res=[]
        for i in word:
            rev=i[::-1]
            res.append(rev)
        return " ".join(res)
        