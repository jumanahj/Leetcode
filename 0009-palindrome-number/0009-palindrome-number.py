class Solution(object):
    def isPalindrome(self, x):
        '''
        s= str(x)
        return s == s[::-1]
        '''
        if x <0:
            return False 
        
        rev=0
        cpy=x

        while x >0:
            rev=rev*10 + x%10
            x=x//10
        if rev == cpy :
            return True 
        return False 