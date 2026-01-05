class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        res=[0]*n
        k = k % n
        j=0
        for i in range(n-k,n):
            res[j]=nums[i]
            j+=1
        for i in range(n-k):
            res[j]=nums[i]
            j+=1

        nums[:] = res
        return nums
       
    '''

         k=k%n
        nums.reverse()
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])
        return nums

        '''


        