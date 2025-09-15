class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        cnt=0
        text=text.split()
        for i in text :
            good=True 
            for j in brokenLetters:
                if j in i :
                    good=False
                    break 
            if good :
                cnt = cnt+1
        return cnt 
            


        

        