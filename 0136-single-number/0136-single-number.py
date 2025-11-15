class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        i=0
        while i<n-1:
            if nums[i]==nums[i+1]:
                i=i+2
            else :
                return nums[i]
        return nums[-1]
        '''
        from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
        '''
        