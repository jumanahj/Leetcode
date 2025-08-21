class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        bin_list=0
        for i in range (len(nums)):
            if bin(i).count("1")== k :
                bin_list=bin_list+nums[i]
        return bin_list
        