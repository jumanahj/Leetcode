class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for num in nums:
            if nums.count(num)==3:
                continue
            else:
                return num
        