class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        s=1
        e=max(piles)
        ans=e
        while s<=e:
            mid= s+(e-s)//2
            hours=0

            for pile in piles:
                hours+=(pile + mid-1)// mid
                #ceil(pile/mid)
            if hours <=h:
                ans=mid
                e= mid-1
            else :
                s=mid+1
        return ans

