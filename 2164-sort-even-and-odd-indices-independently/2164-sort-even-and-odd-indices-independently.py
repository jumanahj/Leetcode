class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        odd=[]
        even =[]
        res=[]
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort(reverse=True)
        even.sort()
        i=j=0
        for k in range(len(nums)):
            if k %2==0:
                res.append(even[i])
                i+=1
            else:
                res.append(odd[j])
                j+=1
        return res
        