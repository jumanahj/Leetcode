class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        peak=nums[0]
        maxele=0
        for i in range(len(nums)):
            if nums[i] > peak:
                maxele = i
                peak=nums[i]
        return maxele
        