class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
    
        c1=self.rob1(nums[:-1])
        c2=self.rob1(nums[1:])

        return max(c1,c2)
        
    def rob1(self,nums):
        prev=0
        curr=0
        for x in nums:
            curr,prev=max(curr,prev+x),curr
        return curr
        