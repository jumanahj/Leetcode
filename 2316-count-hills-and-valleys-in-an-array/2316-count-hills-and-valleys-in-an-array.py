class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hill=0
        valley=0
        arr=[nums[0]]
        for i in nums[1:]:
            if i != arr[-1]:
                arr.append(i)

        for i in range(1,len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                hill=hill+1
            elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                valley=valley+1
        
        return hill+valley
        