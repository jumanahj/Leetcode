class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        tot=sum(nums)
        leftsum=0
        for i in range (len(nums)):
            if leftsum== tot - leftsum-nums[i]:
                return i 
            leftsum += nums[i]
        return -1 