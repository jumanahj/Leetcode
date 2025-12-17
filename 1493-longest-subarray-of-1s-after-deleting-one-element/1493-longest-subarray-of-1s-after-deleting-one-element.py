class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left =0 
        cnt=0
        maxlen=0

        for right in range(len(nums)):
            if nums[right]==0:
                cnt+=1

            while cnt > 1:
                if nums[left]==0:
                    cnt-=1
                left+=1
            maxwind= right-left
            maxlen=max(maxlen,maxwind)

        return maxlen



