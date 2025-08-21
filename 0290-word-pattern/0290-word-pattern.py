class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        sep=s.split()

        if len(pattern) != len(sep):
            return False
        return len(set(pattern))==len(set(sep))==len(set(zip(pattern,sep)))


        