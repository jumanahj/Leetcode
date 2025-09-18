class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        cnt=0
        i=0
        while tickets[k] >0:
            if tickets[i]>0:
                tickets[i]=tickets[i]-1
                cnt=cnt+1
                if i==k and tickets[i]==0:
                    break
            i=(i+1)%len(tickets)
        return cnt 
                

        