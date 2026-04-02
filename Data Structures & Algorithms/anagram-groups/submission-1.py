from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        use the sorted version of the string as the key 
        anyone that matches the key can be added to a new list
        '''
        storage = {}
        for word in strs:
            key = tuple(sorted(word)) # Key to the dictionary
            if key not in storage:
                storage[key] = []
            storage[key].append(word)

        return list(storage.values())
                
