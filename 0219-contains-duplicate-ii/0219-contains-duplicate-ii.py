class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ''''

        for i in range(len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i]==nums[j] and abs(i-j) <= k :
                    return True 
        return False 
        // time limit exceeded 
        '''
        winS=set()
        left=0
        for right in range(len(nums)):
            if nums[right] in winS:
                return True 
            winS.add(nums[right])
            if right-left >=k:
                winS.remove(nums[left])
                left+=1
        return False 



                    
        