class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        uniq=set()
        for num in nums:
            if nums.count(num)==2 and num not in uniq:
                res ^= num
                uniq.add(num)
        return res
        