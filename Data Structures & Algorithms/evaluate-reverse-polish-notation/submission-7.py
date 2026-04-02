class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        will be using a stack to solve this 
        append to the stack until you come accross an operand 
        pop both numbers from the stack 
        append result to your stack 
        repeat and return the last value in the stack             
        '''
        opperands = ['+','-','*','/']
        stack = []
        for num in tokens:
            if num not in opperands:
                stack.append(int(num))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if num == '+':
                    stack.append((num1 + num2))
                if num == '-':
                    stack.append((num2 - num1))
                if num == '/':
                    stack.append(int(num2/num1))
                if num == '*':
                    stack.append((num2 * num1))
        return stack[-1]
            
