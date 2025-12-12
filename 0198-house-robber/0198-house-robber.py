class Solution:
    def rob(self, nums: List[int]) -> int:
        incl=0
        excl=0
        for x in nums:
            new_inc=excl+x
            new_exc=max(excl,incl)

            incl,excl=new_inc,new_exc
        return max(incl,excl)
        
        ''' using dp '''