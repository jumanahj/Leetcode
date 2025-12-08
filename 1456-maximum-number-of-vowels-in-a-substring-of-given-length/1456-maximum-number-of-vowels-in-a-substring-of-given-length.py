class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n=len(s)
        v="aeiou"
        curr=sum(1 for ch in s[:k] if ch in v)
        maxsum=curr

        for i in range(k,n):
            if s[i] in v :
                curr +=1
            if s[i-k] in v:
                curr -=1        
            maxsum=max(maxsum,curr)
        return maxsum
        