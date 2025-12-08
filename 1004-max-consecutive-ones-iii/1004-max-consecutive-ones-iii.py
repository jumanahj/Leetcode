class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        left=0
        zero=0
        maxcons=0
        for right in range(n):
            if nums[right]==0:
                zero+=1

            while zero>k:
                if nums[left] ==0:
                    zero-=1
                left+=1
            curr=right-left+1
            maxcons=max(maxcons,curr)
        return maxcons

        