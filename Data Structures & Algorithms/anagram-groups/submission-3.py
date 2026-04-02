from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        iterate through the array of strings 
        create a key for each unique one 
        group them into a hashmap in this format 
        {
            (a,c,t) = [act,cat]
            (p,o,t,s) = [pots,tops,stop]
        }
        '''
        result = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            if key not in result:
                result[key] = []
            result[key].append(word)
        
        return list(result.values())
