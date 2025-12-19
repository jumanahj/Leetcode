class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            if nums[i] %2 == 0:
                res.append(nums[i])
        
        for i in range(len(nums)):
            if nums[i]%2 !=0:
                res.append(nums[i])
        return res
        