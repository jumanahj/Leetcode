class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        leftmax=[0]*n
        rightmax=[0]*n

        leftmax[0]=height[0]
        rightmax[n-1]=height[n-1]
        res=0

        for i in range(1,n):
            leftmax[i]= max(leftmax[i-1],height[i])

        for i in range(n-2,-1,-1):
            rightmax[i]= max(rightmax[i+1],height[i])
    
        for i in range(1,n):
            res+=min(leftmax[i],rightmax[i])- height[i]
    
        return res 
        
        '''
        n=len(height)
        l,r=0,n-1
        lm=0
        rm=0
        res=0
        while(l<=r):
            if height[l] <= height[r]:
                if height[l] >= lm:
                    lm=height[l]
                else:
                    res+=lm-height[l]
                l+=1
            else:
                if height[r] >= rm:
                    rm=height[r]
                else:
                    res+=rm-height[r]
                r-=1
        return res
    '''
    