class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        arr = list(num)
        i=1
        while i < len(arr) and k  > 0:
            if arr[i-1] > arr[i]:
                arr.pop(i-1)
                k -= 1
                i=max(i-1,1)
            else:
                i+=1
        while k > 0:
            arr.pop()
            k-=1
        res = ''.join(arr).lstrip('0')
        return res if res else "0"
        '''
        stack = []
        if len(num)==k:
            return "0"
        for x in num:
            while stack and stack[-1]>x and k:
                stack.pop()
                k-=1                    
            stack.append(x)

        stack = stack[:len(stack)-k]

        result = ''.join(stack)

        return result.lstrip('0') or "0"
                
                

        