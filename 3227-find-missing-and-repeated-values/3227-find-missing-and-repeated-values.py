class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        seen=set()
        rep=0
        miss=0
        n=len(grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                val=grid[i][j]
                if val in seen:
                    rep=val
                else:
                    seen.add(val)
        
        for num in range(1,n*n+1):
            if num not in seen:
                miss= num 
                break 
        return [rep,miss]

        

        