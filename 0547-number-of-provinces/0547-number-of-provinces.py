class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        vis=[0]*n
        province=0
    
        def dfs(city):
            for i in range(n):
                if isConnected[city][i] == 1 and not vis[i] :
                    vis[i]=1
                    dfs(i)

        for i in range(n):
            if not vis[i]:
                province +=1
                vis[i]=1
                dfs(i)
        return province

        