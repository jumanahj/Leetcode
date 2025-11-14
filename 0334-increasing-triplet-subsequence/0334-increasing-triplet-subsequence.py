class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        firstno=float('inf')
        secondno=float('inf')
        
        for num in nums:
            if num <= firstno:
                firstno=num
            elif num <= secondno:
                secondno=num
            else :
                return True
        return False
            
        