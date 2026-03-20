class Solution:
    def findDiagonalOrder(self, mat):
        m = len(mat)
        n = len(mat[0])
        res = []
        for s in range(m + n - 1):
            temp = []
            for i in range(m):
                j = s - i
                if 0 <= j < n:
                    temp.append(mat[i][j])
            if s % 2 == 0:
                temp.reverse()
            res.extend(temp)
        return res