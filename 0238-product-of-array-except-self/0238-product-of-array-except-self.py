class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        answer=[1]*n

        px=1
        for i in range(n):
            answer[i]=px
            px=px*nums[i]
        
        sx=1
        for i in range(n-1,-1,-1):
            answer[i]*=sx
            sx=sx*nums[i]
        return answer 
        



        '''
        // this takes O(n^2) - time limit exceeded 

        n=len(nums)
        answer=[1]*n

        for i in range (n):
            prod=1
            j=0
            while(j < i):
                prod=prod * nums[j]
                j=j+1

            j=i+1
            while(j < n):
                prod=prod * nums[j]
                j=j+1
            
            answer[i]=prod
        
        return answer
        '''
        



        
        