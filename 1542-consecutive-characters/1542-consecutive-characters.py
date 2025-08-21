class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_cnt=1
        cnt=1
        for i in range(0,len(s)-1):
            if s[i]== s[i+1]:
                cnt+=1
            else:
                cnt=1
            if cnt > max_cnt:
                max_cnt=cnt  
                         
        return max_cnt

        