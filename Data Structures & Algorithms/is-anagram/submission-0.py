class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        strS = sorted(s)
        strT = sorted(t)

        return True if strS == strT else False