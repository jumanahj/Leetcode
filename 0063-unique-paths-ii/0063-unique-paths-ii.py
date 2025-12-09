class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])

        dp=[0]*n
        if obstacleGrid[0][0] == 0:
            dp[0]=1
        else:
            dp[0]=0
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j]=0
                else:
                    if j >0:
                        dp[j]+=dp[j-1]
        return dp[-1]
                
        '''
        def dfs(i,j):
            if i>=m or j>=n:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if i==m-1 and j==n-1:
                return 1

            return dfs(i,j+1)+dfs(i+1,j)
        return dfs(0,0)
        '''

    

        