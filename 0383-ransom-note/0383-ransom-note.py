class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag=Counter(magazine)
        ran=Counter(ransomNote)

        for ch,cnt in ran.items():
            if mag[ch]<cnt:
                return False
        return True 
        '''
        if ran in mag:
            return True
        return False 
        '''
        