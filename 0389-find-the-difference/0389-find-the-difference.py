class Solution(object):
    def findTheDifference(self, s, t):
        
        for ch in t:
            if t.count(ch) > s.count(ch):
                return ch
        

        ''' 
        res=0
        for ch in s+t:
            res ^= ord(ch)
        return chr(res)

        --- using bitwise operation - very fast and interview expected 
        '''

        '''
        sl=list(s)
        tl=list(t)

        for i in tl:
            if i not in sl:
                return i
            else:
                sl.remove(i)
        return ""
        '''
        