class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum_n=sum(nums[:k])
        max_sum=sum_n
        for i in range(k,len(nums)):
            sum_n=sum_n+nums[i]-nums[i-k]
            max_sum=max(max_sum,sum_n)
        return float(max_sum)/k