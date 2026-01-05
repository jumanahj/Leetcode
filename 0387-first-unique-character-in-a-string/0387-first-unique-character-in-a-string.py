class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
 
        unique={}
        for i in s:
            if i not in unique:
                unique[i]=1
            else:
                unique[i]+=1
        for i in range(len(s)):
            if unique[s[i]]==1:
                return i
        return -1

        