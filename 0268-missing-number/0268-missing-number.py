class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        nums.sort()

        '''
        cnt=0

        for i in range(0,n):
            if nums[i] == cnt:
                cnt=cnt+1
            else:
                return cnt
        return n
        '''
        res=n
        for i in range(n):
            res=res^i^nums[i]
        return res



        