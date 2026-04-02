class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Easy way to solve 
        if len(s) != len(t):
            return False
        
        strS = sorted(s)
        strT = sorted(t)

        return True if strS == strT else False
        '''

        # Using Arrays and Hashmaps 
        if len(s) != len(t):
            return False 
        
        sortedS = {}
        sortedT = {}
        # will be storing the count for these letters and check if they are the same
        for i in range(len(s)):
            sortedS[s[i]] = 1 + sortedS.get(s[i],0)
            sortedT[t[i]] = 1 + sortedT.get(t[i],0)
        
        return True if sortedS == sortedT else False 