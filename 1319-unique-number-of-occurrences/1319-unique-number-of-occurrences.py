class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq={}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]= 1 

        count=list(freq.values())
        uniq=set(count)
        if len(uniq)==len(count):
            return True 
        return False 
