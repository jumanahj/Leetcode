class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        revs=s[::-1]
        for i in range(len(s)-1):
            pair=s[i:i+2]
            if pair in revs:
                return True 
        return False 
        

        