class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
            iterate the string forward
            iterate the string backwards as well
            Return false if they are ever not equal to each other

            will need to take out the spaces in the string 
            and then make sure that each string is fully lower case 

            Then you can return True if it is valid
            False if it is not

            Another check I need to make sure of is that I am only appending characters 
            not any other symbol
        '''

        result = ""
        for i in range(len(s)):
            if s[i].isalnum():
                result = result + s[i]

        result = result.replace(" ","")
        result = result.lower()
        print(result)

        forward = 0
        backward = len(result) - 1

        while forward < backward:
            if result[forward] != result[backward]:
                return False
            forward = forward + 1 
            backward = backward - 1
                
        return True
        