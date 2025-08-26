class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i < j < k:
                        val=(nums[i]-nums[j])*nums[k]
                        max_val=max(max_val,val)
        return max_val



        