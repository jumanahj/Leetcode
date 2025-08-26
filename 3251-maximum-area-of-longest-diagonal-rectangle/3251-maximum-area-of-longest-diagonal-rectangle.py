class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_width=0
        max_area=0     
        for l, w in dimensions:
            curr= (l*l)+ (w*w)
            area = l*w 
            if curr>max_width or (curr == max_width and area > max_area):
                max_width=curr
                max_area=area
        return  max_area 


        