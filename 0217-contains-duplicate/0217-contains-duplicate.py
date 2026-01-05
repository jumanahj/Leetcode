class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        un=set(nums)
        if len(un)==len(nums):
            return False 
        return True

        '''
        dict ={}
        for num in nums:
            if num in dict:
                return True
            else:
                dict[num]=1
        return False    
        '''    