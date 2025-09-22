class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        maxf=0
        totf=0

        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1

        for frequ in freq.values():
            if frequ > maxf:
                maxf=frequ
                totf=frequ
            elif frequ ==maxf:
                totf+=frequ
        return totf
        