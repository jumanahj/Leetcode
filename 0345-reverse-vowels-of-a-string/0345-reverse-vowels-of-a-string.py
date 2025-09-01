class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        l=0
        r=len(s)-1
        vowels="aeiouAEIOU"
        while l < r:
            if s[l] not in vowels :
                l+=1
                continue
            if s[r]not in vowels:
                r-=1
                continue
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return "".join(s)
        