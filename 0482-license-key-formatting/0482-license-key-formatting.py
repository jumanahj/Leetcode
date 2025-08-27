class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s=s.replace("-","")
        s=s.upper()

        fg=len(s)%k
        res=[]

        if fg:
            res.append(s[:fg])
        for i in range(fg,len(s),k):
            res.append(s[i:i+k])
        return "-".join(res)

        