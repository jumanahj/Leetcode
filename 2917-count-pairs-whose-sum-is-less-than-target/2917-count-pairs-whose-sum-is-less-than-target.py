class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cnt=0
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] < target and i<j:
                    cnt=cnt+1
        return cnt
        