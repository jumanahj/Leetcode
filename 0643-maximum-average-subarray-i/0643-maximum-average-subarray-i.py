class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Ksum=sum(nums[:k])
        maxsum=Ksum
        for i in range(k,len(nums)):
            Ksum=Ksum+nums[i]-nums[i-k]
            maxsum=max(maxsum,Ksum)
        avg=float(maxsum/k)
        return avg
        