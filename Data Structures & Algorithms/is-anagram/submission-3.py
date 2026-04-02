class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        first s and t have to be the same length
        if this is true 
        we can store the count of each character and then return true 
        if they are both equal 
        '''
        if len(s) != len(t):
            return False

        hashS = {}
        hashT = {}

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i],0)
            hashT[t[i]] = 1 + hashT.get(t[i],0)
        
        return True if hashT == hashS else False

