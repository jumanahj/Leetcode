class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        arra = list(bin(a)[2:].zfill(32))
        arrb = list(bin(b)[2:].zfill(32))
        arrc = list(bin(c)[2:].zfill(32))
        flips=0

        for i in range(31,-1,-1):
            A=int(arra[i])
            B=int(arrb[i])
            C=int(arrc[i])

            if (A|B) == C:
                continue
            if C == 1:
                flips +=1
            else:
                if A==1:
                    flips+=1
                if B==1:
                    flips+=1
        return flips 
           