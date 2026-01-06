class Solution(object):
    def maxArea(self, height):
        
        if len(height) <= 1:
            return 0 

        left=0
        right = len(height)-1
        maxA=0
        
        while left<right :
            w=right-left
            area= min(height[left],height[right])*w
            maxA= max(area , maxA)

            if height[left]<height[right]:
                left+=1
            else :
                right-=1
        return maxA