class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        coll=1 
        while coll:
            coll=0
            i=0
            res=[]
            while i < len(asteroids):
                if i <len(asteroids)-1 and asteroids[i]>0 and asteroids[i+1]<0:
                    if abs(asteroids[i])>abs(asteroids[i+1]):
                        res.append(asteroids[i])
                    elif abs(asteroids[i])<abs(asteroids[i+1]):
                        res.append(asteroids[i+1])
                    i=i+2
                    coll=1
                else:
                    res.append(asteroids[i])
                    i=i+1
            asteroids=res
        return asteroids
                