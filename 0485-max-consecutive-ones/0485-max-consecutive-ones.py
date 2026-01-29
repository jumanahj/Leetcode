class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxones=0
        cnt=0

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt +=1
            else:
                cnt = 0
            maxones = max(maxones,cnt)
        return maxones

        