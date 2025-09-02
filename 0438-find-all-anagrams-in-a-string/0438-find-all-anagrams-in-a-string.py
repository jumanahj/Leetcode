class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res=[]
        k=len(p)
        pcnt=Counter(p)
        scnt=Counter(s[:k-1])

        for i in range(k-1,len(s)):
            scnt[s[i]]+=1
            if scnt==pcnt:
                res.append(i-k+1)
            l=s[i-k+1]
            scnt[l]-=1
            if scnt[l]==0:
                del scnt[l]
        return res 