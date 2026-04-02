class Solution:
    def isValid(self, s: str) -> bool:
        
        '''
        every closing bracket must have a corresponding opening bracket 
        if we come accross a closing bracket and our stack is empty,
        we return False 
        else we pop from the stack
        at the end, the stack should be empty and we can return True 
        '''
        
        pancake = []
        
        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for br in s:
            if br in brackets:
                #coming accross a closing bracket. The key of hashmap is br 
                if not pancake or brackets[br] != pancake[-1]:
                    return False
                else:
                    # we come accross a situation where brackets[br] == pancake at the end
                    pancake.pop()
            else:
                #opening brackets
                pancake.append(br)
        
        return not pancake

        