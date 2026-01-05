class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        cnt=0
        summ=0
        minval=float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]<0:
                    cnt=cnt+1
                summ=summ+abs(matrix[i][j])
                minval=min(minval,abs(matrix[i][j]))
        if cnt %2==0:
            return summ
        else :
            return summ-2*minval

            '''
        if odd number of elemnts are negative - even after multiplying well have one odd number of element , so try to keep the small element as negative one , 
        then add all other numbers and return sum 

        Find the absolute sum of all the numbers in the matrix
Find the absolute value of the smallest number in the matrix
Count of negative numbers in the matrix
If count of negatives is even, then all elements can be made +ve by performing the operation, so just return sum
If count of negatives is odd, then we can make the smallest number in the matrix as -ve and then return sum
'''
        