class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_pow=1
        cnt=1

        for i in range(1,len(s)):
            if s[i]== s[i-1]:
                cnt+=1
            else:
                cnt=1
            max_pow=max(max_pow,cnt)
        return max_pow

        