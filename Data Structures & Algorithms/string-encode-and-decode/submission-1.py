class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded = encoded + str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        '''
        essentially I want to extract the words into
        the decoded list
        '''
        decoded = []
        '''
        5#Hello5#World
        will loop until a hashtag is found
        once found will add the count of what comes before it to my list
        '''
        i = 0
        j = 0
        while i < len(s):
            if s[i] != '#':
                i = i + 1
            else:
                num = int(s[j:i])
                j = i + num + 1
                start = i + 1
                end = j
                decoded.append(s[start:end])
                i = j
        
        return decoded



