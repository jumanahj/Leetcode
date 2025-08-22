class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        cnt=0
        num1=num
        while(num1>0):
            val=num1%10
            if num%val==0:
                cnt=cnt+1
            num1=num1//10
        return cnt