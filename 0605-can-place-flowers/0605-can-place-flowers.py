class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        poss=0
        if n==0:
            return True 

        for i in range(0,len(flowerbed)):
            if flowerbed[i]==0:
                left = (i==0 ) or (flowerbed[i-1] ==0 )
                right =(i==len(flowerbed)-1) or (flowerbed[i+1]) == 0 

                if left and right:
                    flowerbed[i] = 1  
                    n -= 1         
                    if n == 0:
                        return True   

        return False
                    

                    
                