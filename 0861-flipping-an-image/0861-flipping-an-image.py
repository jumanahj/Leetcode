class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        r=len(image)
        c=len(image[0])
        for i in range(r):
            image[i]=image[i][::-1]
            for j in range(c):
                image[i][j]=1-image[i][j]
        return image