class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        for this we will use the two pointer solution
        spelled forward should be spelled the same backwards
        want to consider only alphanumeric characters 
        so A-Z and 0-9
        '''
        l = 0 
        r = len(s) - 1 
        while l <= r:
            '''
            need to check for alphanumeric characters only
            '''
            if not s[l].isalnum():
                l = l + 1
                continue
            if not s[r].isalnum():
                r = r - 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l = l + 1 
            r = r - 1
        
        return True
            