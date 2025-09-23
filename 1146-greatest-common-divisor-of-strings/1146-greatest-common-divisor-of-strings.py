class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 +str1:
            return ""

        maxl=gcd(len(str1),len(str2))
        return str1[:maxl]
        '''

        if len(str1) > len(str2):
            if str2 in str1 :
                return str2
        if len(str2)>len(str1):
            if str1 in str2 :
                return str1
        else:
            return ""
        '''
        