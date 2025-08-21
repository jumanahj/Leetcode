class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        res=list(set(nums1)&set(nums2))
        res.sort()
        if len(res)==0:
            return -1
        else :
            return res[0]

        