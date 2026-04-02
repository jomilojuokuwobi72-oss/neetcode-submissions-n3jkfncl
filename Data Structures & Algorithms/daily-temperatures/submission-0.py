class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        initialize result as a list of zeroes the length of temperatures 
        initialize a stack as well that will store both temp and index 
        iterate through the array:
            while stack is not empty and the next number is greater than top:
                pop from stack and calculate the difference 
                update the result accordingly 
            if not we add the next number to the stack 
        
        return result 
        '''
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndx = stack.pop()
                result[stackIndx] = i - stackIndx
            stack.append([temp,i])

        return result            