class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        '''
        max_val=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i < j < k:
                        val=(nums[i]-nums[j])*nums[k]
                        max_val=max(max_val,val)
        return max_val
        '''
        ans=0
        max_diff=0
        max_num=0
        for num in nums:
            ans=max(ans,max_diff*num)
            max_diff=max(max_diff,max_num-num)
            max_num=max(max_num,num)
        return ans


