class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        res=[0]*n
        cnt=0
        op=0
        for i in range(n):
            res[i]+=op
            if boxes[i]=="1":
                cnt+=1
            op+=cnt
            
        cnt=0
        op=0
        for i in range(n-1,-1,-1):
            res[i]+=op
            if boxes[i]=="1":
                cnt+=1
            op+=cnt
        return res
            
        