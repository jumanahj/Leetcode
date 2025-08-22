class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        lower=bool(re.search(r"[a-z]",password))
        upper=bool(re.search(r"[A-Z]",password))
        digits=bool(re.search(r"[0-9]",password))
        special= "!@#$%^&*()-+"

        if len(password)<8:
            return False

        if not (lower and upper and digits and any(ch in special for ch in password)):
            return False 
        
        
        for i in range(1,len(password)):
            if password[i]==password[i-1]:
                return False 
            
        return True 